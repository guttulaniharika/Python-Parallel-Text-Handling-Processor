🚀 Parallel Text Processing & Sentiment Analysis System

A high-performance, scalable, parallel text processing system built in Python that performs sentiment analysis, chunk-based processing, search, visualization, and reporting using modern optimization techniques.

This system is designed to efficiently handle large-scale datasets (50K – 1M+ records) using multiprocessing, chunking, and optimized data pipelines.

---

📌 Features at a Glance

⚡ Parallel Processing using Multiple CPU Cores
📦 Chunk-Based Large Dataset Handling
🧠 Rule-Based Sentiment Analysis Engine
📊 Interactive Streamlit Dashboard
🔍 Keyword Search with Matching Results
📤 CSV Export Functionality
📧 Email Summary Integration (SMTP)
📈 Data Visualization (Bar & Pie Charts)
🔄 Reset & Session Management
⚙️ Edge Case Handling (Empty / Invalid Files)
🧩 Modular & Extensible Architecture

---

📂 Project Folder Structure

PythonParallelTextProcessor/
│
├── app.py                     # 🌐 Streamlit UI Application
├── main.py                    # 🚦 Backend execution entry
├── processor.py               # ⚙️ Core processing logic
├── chunk_manager.py           # 📦 Chunk handling module
├── sentiment_rules.py         # 🧠 Sentiment analysis rules
├── db_manager.py              # 💾 Database operations (SQLite)
├── generator.py               # 🧪 Dataset generator
│
├── Dataset.csv                # 📄 Input dataset
├── sentiment_dataset_5000.csv
├── output_results.csv         # 📊 Processed output
├── project.db                 # 🗄 Database file
│
├── .streamlit/config.toml     # ⚙️ Streamlit config
├── README.md
└── LICENSE

---

🧠 Project Overview

This system processes large text datasets using parallel execution and chunk-based processing, applies rule-based sentiment scoring, and provides:

👉 End-to-End Processing Pipeline
👉 Interactive Dashboard (Streamlit UI)
👉 Search, Export, and Email Capabilities

The system is optimized for:

- Sentiment analysis
- Text analytics
- Large-scale data processing

---

🏗 System Architecture

User Input (Upload File)
        ↓
File Preview & Validation
        ↓
Data Extraction Layer
        ↓
Chunk Creation Module
        ↓
Parallel Processing Engine (Multiprocessing)
        ↓
Sentiment Analysis Engine
        ↓
Result Aggregation
        ↓
Dashboard Visualization
        ↓
Search / Export / Email Output

---

🚀 End-to-End Workflow

When the user runs the application:

1️⃣ Upload CSV / TXT / Excel file
2️⃣ System reads and extracts text column
3️⃣ Data is divided into chunks
4️⃣ Each chunk is processed in parallel
5️⃣ Sentiment score is calculated
6️⃣ Results are stored and aggregated
7️⃣ Dashboard displays analytics
8️⃣ User can search, download, or email results

---

📦 Chunk Processing

Large datasets are divided into smaller chunks for efficiency.

Example:

Dataset Size| Chunk Size| Chunks
50,000| 1,000| 50
100,000| 10,000| 10
1,000,000| 10,000| 100

✔ Reduces memory usage
✔ Improves scalability

---

🚀 Parallel Processing

Implemented using:

multiprocessing.Pool(cpu_count())

How it works:

- Data is divided into parts
- Each CPU core processes part of the data
- All cores run simultaneously
- Results are combined

Benefit:

✔ Faster execution
✔ Efficient CPU utilization

---

🧠 Sentiment Analysis Engine

Rule-Based Approach

Uses predefined word lists.

Positive Words

good, great, excellent, happy

Negative Words

bad, terrible, worst

---

📊 Score Formula

Score = Positive Count − Negative Count

---

🏷 Sentiment Classification

Score| Sentiment
> 0| Positive
< 0| Negative
= 0| Neutral

---

📊 Dashboard Features

- Total records processed
- Positive / Negative / Neutral counts
- CPU cores used
- Processing time

---

📈 Visualization

- 📊 Bar Chart
- 🥧 Pie Chart

---

🔍 Search Engine

- Keyword-based search
- Shows matching results
- Calculates sentiment summary

---

📧 Email Module

- Sends results using SMTP
- Includes:
  - Keyword
  - Sentiment counts
  - Processing time

---

📤 Export Module

- Download results as CSV
- Includes:
  - Text
  - Score
  - Sentiment

---

⚡ Performance Analysis

Processing Comparison

Method| Performance
Single Processing| Slow
Threading| Medium
Multiprocessing| Fast 🚀

---

Example:

Single Processing: 7.62 sec
Thread Processing: 12.00 sec
Multiprocessing: 1.51 sec

---

📊 Sentiment Distribution

Example Output:

Positive : 32638
Negative : 9857
Neutral  : 7505

---

💾 Database Integration

- SQLite database ("project.db")
- Stores processed results
- Supports query optimization

---

📌 Project Milestones

🟢 Milestone 1 — Core System

✔ Data loading
✔ Sentiment analysis
✔ Chunk processing

---

🟢 Milestone 2 — Optimization

✔ Threading
✔ Multiprocessing
✔ Performance benchmarking

---

🟢 Milestone 3 — UI Development

✔ Streamlit dashboard
✔ Charts & visualization
✔ Search & export

---

🟢 Milestone 4 — Advanced Features

✔ Parallel + chunk integration
✔ Large dataset handling
✔ CPU core utilization
✔ Edge case handling

---

⚠️ Limitations

- Upload size limited (~200MB default)
- Large files require configuration

---

🔮 Future Enhancements

- Cloud integration (AWS / GCP)
- Real-time streaming
- ML-based sentiment models
- API support (FastAPI)

---

🛠 Tech Stack

Component| Technology
Language| Python
UI| Streamlit
Data Handling| Pandas
Visualization| Matplotlib
Database| SQLite
Parallelism| Multiprocessing
Email|SMTP

---

👩‍💻 Author

Niharika Devi Guttula
B.Tech | Aspiring Software Engineer

---

📜 License (MIT)

MIT License

Copyright (c) 2026 Niharika Devi Guttula

