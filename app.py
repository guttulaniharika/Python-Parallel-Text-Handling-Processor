import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import time
from multiprocessing import Pool, cpu_count

from sentiment_rules import clean_text, analyze_sentiment


# -------- EMAIL FUNCTION --------
def send_email(receiver, content):
    sender = "guttulaniharikadevi@gmail.com"
    password = "sftnmfambzliielo"

    msg = MIMEText(content)
    msg["Subject"] = "Keyword Sentiment Result"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        return str(e)


# -------- PARALLEL FUNCTION --------
def process_text(t):
    cleaned = clean_text(str(t))
    score, sentiment = analyze_sentiment(cleaned)
    return [t, score, sentiment]


# -------- CHUNK FUNCTION --------
def create_chunks(data, size=50):
    return [data[i:i+size] for i in range(0, len(data), size)]


# -------- PAGE CONFIG --------
st.set_page_config(page_title="Text Processing System", layout="wide")


# -------- CSS --------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #020617, #0F172A, #1E1B4B);
}
.stButton>button {
    background: linear-gradient(135deg, #6366F1, #8B5CF6, #EC4899);
    color: white;
    border-radius: 14px;
}
.card {
    padding: 20px;
    border-radius: 18px;
    background: rgba(255,255,255,0.05);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# -------- TITLE --------
st.markdown("""
<h1 style='text-align:center;'>🚀 Parallel Text Processing</h1>
<p style='text-align:center; color:#9CA3AF;'>Sentiment Dashboard ✨</p>
""", unsafe_allow_html=True)


# -------- HERO --------
st.markdown("""
<div class="card">
<h3>📊 Smart Text Analytics</h3>
<p>Upload → Analyze → Visualize → Download</p>
</div>
""", unsafe_allow_html=True)


# -------- SIDEBAR --------
uploaded_file = st.sidebar.file_uploader("Upload CSV/TXT/Excel", type=["csv","txt","xlsx"])
start_button = st.sidebar.button("🚀 Start Processing")

if uploaded_file:
    st.sidebar.write("📁 1 file uploaded")

if st.sidebar.button("🔄 Reset"):
    st.session_state.clear()


# -------- PREVIEW --------
if uploaded_file:
    st.markdown("## 📂 File Preview")

    uploaded_file.seek(0)

    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(uploaded_file)
        st.dataframe(df.head())

    else:
        text = uploaded_file.read().decode("utf-8")
        st.text(text[:500])


# -------- PROCESSING --------
if uploaded_file and start_button:

    start_time = time.time()

    st.markdown("## ⚙️ Processing...")
    progress = st.progress(0)

    uploaded_file.seek(0)

    # -------- READ FILE --------
    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(uploaded_file)

    else:
        text = uploaded_file.read().decode("utf-8")
        texts = [line for line in text.split("\n") if line.strip()]

    # -------- EMPTY CHECK --------
    if uploaded_file.type != "text/plain":

        if df.empty:
            st.warning("⚠️ Empty file uploaded")
            st.stop()

        if "text" in df.columns:
            texts = df["text"]
        elif "review" in df.columns:
            texts = df["review"]
        elif "content" in df.columns:
            texts = df["content"]
        else:
            st.error("No valid text column")
            st.stop()

    if len(texts) == 0:
        st.warning("⚠️ Empty file uploaded")
        st.stop()

    total_lines = len(texts)

    # -------- PARALLEL PROCESSING --------
    with st.spinner("Processing in parallel..."):
        with Pool(cpu_count()) as p:
            results = p.map(process_text, texts)

    progress.progress(100)

    # -------- RESULT DF --------
    result_df = pd.DataFrame(results, columns=["Text","Score","Sentiment"])


    # -------- CHUNK ANALYSIS --------
    chunks = create_chunks(texts, 50)
    chunk_results = []

    for idx, chunk in enumerate(chunks):

        scores = []

        for line in chunk:

            if pd.isna(line) or str(line).strip() == "":
                continue

            cleaned = clean_text(str(line))
            score, _ = analyze_sentiment(cleaned)

            scores.append(score)

        avg = sum(scores)/len(scores) if len(scores) > 0 else 0

        sentiment = "Positive" if avg > 0 else "Negative" if avg < 0 else "Neutral"

        chunk_results.append([idx+1, len(chunk), round(avg,2), sentiment])

    chunk_df = pd.DataFrame(
        chunk_results,
        columns=["Chunk ID","Lines","Avg Score","Chunk Sentiment"]
    )


    processing_time = round(time.time() - start_time, 2)

    st.success("✅ Processing Completed!")

    # SAVE
    st.session_state["result_df"] = result_df
    st.session_state["chunk_df"] = chunk_df
    st.session_state["processing_time"] = processing_time


# -------- DISPLAY --------
if "result_df" in st.session_state:

    result_df = st.session_state["result_df"]
    chunk_df = st.session_state["chunk_df"]

    st.markdown("## 📊 Dashboard")

    st.write(f"Total Records Processed: {len(result_df)}")
    st.write(f"CPU Cores Used: {cpu_count()}")

    pos = (result_df["Sentiment"]=="Positive").sum()
    neg = (result_df["Sentiment"]=="Negative").sum()
    neu = (result_df["Sentiment"]=="Neutral").sum()

    col1,col2,col3,col4 = st.columns(4)
    col1.metric("Total", len(result_df))
    col2.metric("Positive", pos)
    col3.metric("Negative", neg)
    col4.metric("Neutral", neu)


    st.markdown("## 📄 Line level Results")
    st.dataframe(result_df)

    st.markdown("## 📦 Chunk Analysis")
    st.dataframe(chunk_df)


    # -------- CHARTS --------
    col1,col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots()
        ax.bar(["Positive","Negative","Neutral"], [pos,neg,neu])
        st.pyplot(fig)

    with col2:
        fig2, ax2 = plt.subplots()
        ax2.pie([pos,neg,neu], labels=["Positive","Negative","Neutral"], autopct="%1.1f%%")
        st.pyplot(fig2)


    # -------- SEARCH --------
    st.markdown("## 🔍 Search")

    keyword = st.text_input("Enter keyword")

    if keyword:

        words = keyword.lower().split()

        p=n=u=0
        for w in words:
            _, s = analyze_sentiment(w)
            if s=="Positive": p+=1
            elif s=="Negative": n+=1
            else: u+=1

        total = p-n
        final = "Positive" if p>n else "Negative" if n>p else "Neutral"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        processing_time = st.session_state.get("processing_time",0)

        st.write(f"Positive Count: {p}")
        st.write(f"Negative Count: {n}")
        st.write(f"Neutral Count: {u}")
        st.write(f"Total Score: {total}")
        st.write(f"Final Sentiment: {final}")
        st.write(f"Timestamp: {timestamp}")
        st.write(f"Processing Time: {processing_time} seconds")
        st.write("")


        # -------- MATCHING --------
        filtered = result_df[
            result_df["Text"].str.lower().str.contains('|'.join(words))
        ]

        st.markdown("### 📄 Matching Results")

        if len(filtered)>0:
            st.dataframe(filtered)
        else:
            st.warning("No matching results")


        # -------- EMAIL --------
        st.markdown("## 📧 Send Results via Email")

        email = st.text_input("Enter Email")

        if st.button("Send Email"):

            summary = f"""
Keyword: {keyword}
Positive: {p}
Negative: {n}
Neutral: {u}
Final: {final}
Time: {timestamp}
Processing Time: {processing_time}
"""

            res = send_email(email, summary)

            if res==True:
                st.success("Email sent")
            else:
                st.error(res)


    # -------- DOWNLOAD --------
    csv = result_df.to_csv(index=False).encode()
    st.download_button("Download CSV Report", csv, "results.csv")