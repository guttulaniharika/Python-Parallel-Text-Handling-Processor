
🚀 Parallel Text Processing & Sentiment Analysis System

A high-performance, scalable Python-based system designed to process large text datasets using parallel processing, chunk-based execution, and rule-based sentiment analysis.

---

📌 Features at a Glance

Parallel Processing using multiple CPU cores
Chunk-Based Processing for large datasets
Rule-Based Sentiment Analysis engine
Streamlit interactive dashboard
File Upload support (CSV, TXT, Excel)
File preview before processing
Keyword search with matching results
CSV export functionality
Email summary using SMTP
Bar chart and pie chart visualization
Processing time tracking
CPU core usage display
Reset / clear data functionality
Edge case handling (empty and invalid files)

---

📂 Project Structure

PythonParallelTextProcessor/

app.py — Streamlit UI application
main.py — Backend execution script
processor.py — Core processing logic
chunk_manager.py — Chunk creation module
sentiment_rules.py — Sentiment analysis rules
db_manager.py — Database operations
generator.py — Dataset generator

Dataset.csv — Input dataset
sentiment_dataset_5000.csv — Sample dataset
output_results.csv — Processed results
project.db — SQLite database

.streamlit/config.toml — Streamlit configuration
README.md — Documentation
LICENSE — MIT License

---

🧠 Project Overview

This system processes large text datasets efficiently by combining parallel processing and chunk-based techniques. It performs sentiment analysis and provides visualization, search, and export functionalities.

---

🏗 System Architecture

User Input
→ File Upload & Validation
→ Data Extraction
→ Chunk Creation
→ Parallel Processing
→ Sentiment Analysis
→ Result Aggregation
→ Dashboard Visualization
→ Search / Export / Email Output

---

🚀 End-to-End Workflow

User uploads file (CSV / TXT / Excel)
→ System validates file
→ Displays preview
→ Extracts text data
→ Divides data into chunks
→ Assigns chunks to CPU cores
→ Processes data in parallel
→ Calculates sentiment score
→ Combines results
→ Displays dashboard metrics
→ Allows search, download, and email

---

📦 Chunk Processing

Large datasets are divided into smaller chunks to improve performance and reduce memory usage.

Example:

50,000 records → chunk size 1,000 → 50 chunks
100,000 records → chunk size 10,000 → 10 chunks
1,000,000 records → chunk size 10,000 → 100 chunks

---

🚀 Parallel Processing

Implemented using multiprocessing:

Pool(cpu_count())

Data is divided and assigned to multiple CPU cores
Each core processes its part simultaneously
Results are combined after processing

Benefit:
Faster execution and efficient CPU utilization

---

🧠 Sentiment Analysis Logic

Rule-based approach using predefined word lists

Positive words: good, great, excellent, happy
Negative words: bad, terrible, worst

Score = Positive Count − Negative Count

Sentiment classification:

Score > 0 → Positive
Score < 0 → Negative
Score = 0 → Neutral

---

📊 Dashboard Output

Total records processed
Positive count
Negative count
Neutral count
CPU cores used
Processing time

---

📈 Visualization

Bar chart for sentiment comparison
Pie chart for sentiment distribution

---

🔍 Search Module

User enters keyword
System finds matching rows
Displays sentiment summary and results

---

📧 Email Module

Sends summary to user email
Includes sentiment counts and processing time

---

📤 Export Module

Download processed results as CSV file

---

⚡ Performance Comparison

Single Processing → slow
Thread Processing → moderate
Multiprocessing → fastest

Example:

Single: 7.62 sec
Thread: 12 sec
Multiprocessing: 1.51 sec

---

📊 Sentiment Distribution Example

Positive: 32638
Negative: 9857
Neutral: 7505

---

💾 Database Integration

SQLite database (project.db)

Stores:
id, text, score, sentiment

---

📌 Project Milestones

Milestone 1:
Dataset loading
Sentiment analysis
Chunk processing

Milestone 2:
Thread processing
Multiprocessing
Performance comparison

Milestone 3:
Streamlit UI
Dashboard visualization
Search and export

Milestone 4:
Large dataset handling
Parallel optimization
CPU utilization
Edge case handling



---

🔮 Future Enhancements

Cloud integration (AWS / Google Drive)
Real-time processing
Machine learning-based sentiment analysis
API integration

---

🛠 Tech Stack

Python
Streamlit
Pandas
Matplotlib
SQLite
Multiprocessing

---

👩‍💻 Author

Niharika Devi Guttula

---

📜 License

MIT License

Copyright (c) 2026 Niharika Devi Guttula

