🚀 Parallel Text Processing & Sentiment Analysis Platform

A high-performance, scalable system for analyzing large-scale text datasets using parallel processing, chunk-based computation, and rule-based sentiment analysis.

This project combines:

- 🌐 Interactive Web Application (Streamlit UI)
- ⚙️ Backend Processing Engine with Performance Benchmarking
- 💾 Database Storage & Query Optimization

---

📖 Abstract

With the exponential growth of textual data, efficient processing becomes critical. This system is designed to handle large datasets (50K – 1M+ records) by leveraging:

- Parallel execution using multiple CPU cores
- Chunk-based memory-efficient processing
- Lightweight rule-based NLP for sentiment classification

The platform provides real-time analytics, visualization, and export capabilities.

---

🎯 Objectives

- Efficiently process large text datasets
- Reduce execution time using parallel computing
- Optimize memory usage via chunk processing
- Provide real-time visualization and insights
- Benchmark different processing techniques

---

✨ Core Features

📂 Data Ingestion Module

- Supports CSV, TXT, XLSX formats
- Dynamic file preview
- Input validation (empty/invalid files)

---

⚙️ Processing Engine

- Text preprocessing (cleaning & normalization)
- Rule-based sentiment scoring
- High-performance batch execution

---

🚀 Parallel Computing Layer

- Built using Python "multiprocessing"
- Auto-detects system cores via "cpu_count()"
- Distributes workload across cores
- Achieves significant speed improvement

---

📦 Chunk Processing Strategy

- Splits large datasets into smaller chunks
- Enables scalable and memory-efficient execution
- Prevents system overload for large inputs

---

📊 Analytics & Visualization

- KPI Metrics:
  - Total records
  - Sentiment distribution
- Graphs:
  - Bar chart
  - Pie chart

---

🔍 Search & Query Module

- Keyword-based filtering
- Real-time matching results
- Sentiment breakdown per query

---

📧 Notification Module

- SMTP-based email integration
- Sends processed insights to users

---

📥 Export Module

- Download processed dataset (CSV)

---

💾 Persistence Layer

- SQLite database ("project.db")
- Structured storage of processed results
- Query performance optimization using indexing

---

🧠 System Architecture

User Input Layer
        ↓
File Upload & Validation
        ↓
Data Extraction Layer
        ↓
Chunk Manager
        ↓
Parallel Processing Engine
        ↓
Sentiment Analysis Module
        ↓
Database Storage (SQLite)
        ↓
Visualization & Dashboard
        ↓
Search / Export / Email

---

📁 Project Structure

PythonParallelTextProcessor/
│
├── app.py                 # 🌐 Streamlit UI
├── main.py                # 🚦 Backend entry point
├── processor.py           # ⚙️ Core processing logic
├── chunk_manager.py       # 📦 Chunk creation
├── sentiment_rules.py     # 🧠 Sentiment engine
├── db_manager.py          # 💾 Database handler
├── generator.py           # 🧪 Dataset generator
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

⚙️ Execution Guide

git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
streamlit run app.py

---

⚡ Performance Optimization

🔹 Parallel Processing

- Utilizes all available CPU cores
- Reduces execution time significantly

🔹 Chunk Processing

- Processes data in manageable blocks
- Prevents memory overflow

---

📊 Performance Benchmark

Method| Execution Time
Single Processing| Slow
Threading| Moderate
Multiprocessing| Fastest 🚀

Example:

- Single → 7.62 sec
- Thread → 12 sec
- Multiprocessing → 1.51 sec

---

📦 Scalability Example

Records| Chunk Size| Chunks
50,000| 1,000| 50
100,000| 10,000| 10
1,000,000| 10,000| 100

---

🧠 Sentiment Analysis Model

Rule-Based Approach

Score Formula:

Score = Positive Count − Negative Count

Classification:

Score| Sentiment
> 0| Positive
< 0| Negative
= 0| Neutral

---

📊 Sample Output

Total Records: 60000
Total Chunks: 60

Fastest Method: Multiprocessing

Sentiment Distribution:
Positive: 44.6%
Negative: 44.1%
Neutral: 11.3%

---

💾 Database Optimization

- Stores processed results
- Improves query performance using indexing

Example:

- Before Index → 0.173 sec
- After Index → 0.154 sec

---

📌 Development Milestones

🟢 Phase 1: Core Processing

- Data loading
- Sentiment logic
- Chunk implementation

🟢 Phase 2: Performance Optimization

- Threading
- Multiprocessing
- Benchmarking

🟢 Phase 3: UI Development

- Streamlit interface
- Dashboard & charts
- Search & export

🟢 Phase 4: Advanced Optimization

- Parallel + chunk integration
- Large dataset handling (100K+)
- CPU utilization
- Edge case handling

---

⚠️ Limitations

- Default upload limit (~200MB)
- Requires scaling for 1GB+ datasets

---

🔮 Future Scope

- Cloud integration (AWS / GCP)
- Real-time streaming pipelines
- ML/DL-based sentiment models
- Multi-user support

---

🛠 Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib
- SQLite
- Multiprocessing

---

👩‍💻 Author

Niharika Devi Guttula
B.Tech | Aspiring Software Engineer

---

📜 License

MIT License

Copyright (c) 2026 Niharika Devi Guttula

