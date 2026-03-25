🚀 Parallel Text Processing & Sentiment Analysis System

A high-performance, scalable, multiprocessing-based text processing system built in Python for efficient handling of large datasets using chunk-based execution and rule-based sentiment analysis.

This system is designed for fast batch processing, parallel text computation, real-time analytics, and an interactive Streamlit dashboard — optimized for large-scale data workflows.

---

⭐ Features at a Glance

⭐ Parallel Processing Engine (Multiprocessing)
⭐ Chunk-Based Data Processing for Large Datasets
⭐ Rule-Based Sentiment Analysis Engine
⭐ Streamlit Interactive Dashboard
⭐ File Upload (CSV, TXT, Excel) with Preview
⭐ Keyword Search with Matching Results
⭐ CSV Export Functionality
⭐ Email Summary Integration (SMTP)
⭐ Data Visualization (Bar Chart & Pie Chart)
⭐ CPU Core Utilization Tracking
⭐ Processing Time Monitoring
⭐ Reset & Session Management
⭐ Robust Edge Case Handling
⭐ Modular and Extensible Architecture

---

📁 Project Folder Structure

PythonParallelTextProcessor/
│
├── app.py
├── main.py
├── processor.py
├── chunk_manager.py
├── sentiment_rules.py
├── db_manager.py
├── generator.py
│
├── Dataset.csv
├── sentiment_dataset_5000.csv
├── output_results.csv
├── project.db
│
├── .streamlit/config.toml
├── README.md
└── LICENSE

---

🧠 Project Overview

This system processes large text datasets efficiently by combining parallel execution and chunk-based strategies. It performs sentiment analysis and provides visualization, search, and export functionalities through an intuitive interface.

---

🏗 System Architecture

User Input → File Upload & Validation → Data Extraction → Chunk Segmentation → Parallel Processing Engine → Sentiment Analysis → Result Aggregation → Dashboard Visualization → Search / Export / Email Output

---

🚀 End-to-End Workflow

User uploads dataset → System validates input → Displays preview → Extracts text → Divides into chunks → Assigns chunks to CPU cores → Processes in parallel → Calculates sentiment → Aggregates results → Displays dashboard → Enables search, export, and email

---

📦 Chunk Processing

Large datasets are divided into smaller chunks to improve performance and reduce memory usage

50,000 records → 1,000 per chunk → 50 chunks
100,000 records → 10,000 per chunk → 10 chunks
1,000,000 records → 10,000 per chunk → 100 chunks

---

🚀 Parallel Processing

Implemented using multiprocessing

Pool(cpu_count())

Data is divided → Assigned to CPU cores → Executed simultaneously → Results combined

This reduces execution time and improves efficiency

---

🧠 Sentiment Analysis Engine

Rule-based approach using predefined word patterns

Positive words: good, great, excellent, happy
Negative words: bad, terrible, worst

Score = Positive Count − Negative Count

Score > 0 → Positive
Score < 0 → Negative
Score = 0 → Neutral

---

📊 Dashboard Analytics

Total records processed
Positive, Negative, Neutral counts
CPU cores used
Processing time

---

📈 Visualization

Bar chart for sentiment comparison
Pie chart for sentiment distribution

---

🔍 Search Module

Keyword-based search → Displays matching results → Shows sentiment summary

---

📧 Email Module

Sends structured summary including sentiment counts and processing details

---

📤 Export Module

Download processed dataset as CSV file

---

⚡ Performance Benchmark

Single Processing → slow
Thread Processing → moderate
Multiprocessing → fastest

Example:

Single 7.62 sec
Thread 12 sec
Multiprocessing 1.51 sec

---

💾 Database Layer

SQLite database (project.db)

Stores: id, text, score, sentiment

---

📌 Milestones

Milestone 1 — Data loading, preprocessing, sentiment analysis, chunking
Milestone 2 — Threading, multiprocessing, performance benchmarking
Milestone 3 — Streamlit UI, dashboard, search, export
Milestone 4 — Large dataset optimization, CPU utilization, edge cases

---

⚠️ Limitations

File upload limit ~200MB
Large files require configuration or cloud storage

---

🔮 Future Enhancements

Cloud integration (AWS / GCP)
Real-time streaming processing
Machine learning-based sentiment models
API development (FastAPI)

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
