# 🚀 Parallel Text Processing & Sentiment Analysis System

<p align="center">
  <b>High-Performance • Scalable • Parallel Computing • Real-Time Analytics</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Multiprocessing-Enabled-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

---

## 📌 Overview

A **high-performance text processing system** built in Python to efficiently handle **large-scale datasets** using:

* ⚡ Parallel Processing (Multiprocessing)
* 📦 Chunk-Based Execution
* 🧠 Rule-Based Sentiment Analysis

The system delivers **fast batch processing, real-time insights, and an interactive Streamlit dashboard**, making it ideal for large text workflows and analytics applications.

---

## 📚 Table of Contents

* [✨ Features](#-features)
* [📁 Project Structure](#-project-structure)
* [⚙️ Installation](#️-installation)
* [🚀 Usage](#-usage)
* [🏗 Architecture](#-architecture)
* [⚡ Workflow](#-workflow)
* [📦 Processing Strategy](#-processing-strategy)
* [🧠 Sentiment Engine](#-sentiment-engine)
* [📊 Dashboard](#-dashboard)
* [📈 Performance](#-performance)
* [💾 Database](#-database)
* [📌 Milestones](#-milestones)
* [⚠️ Limitations](#️-limitations)
* [🔮 Future Scope](#-future-scope)
* [🛠 Tech Stack](#-tech-stack)
* [👩‍💻 Author](#-author)
* [📜 License](#-license)

---

## ✨ Features

* ⚡ High-speed **parallel processing engine**
* 📦 Efficient **chunk-based dataset handling**
* 🧠 Custom **rule-based sentiment scoring**
* 📊 Interactive **Streamlit dashboard**
* 📁 File upload with preview (CSV / TXT)
* 🔍 Advanced keyword search
* 📤 Export processed results (CSV)
* 📈 Visual analytics (Bar & Pie charts)
* 🖥 CPU utilization monitoring
* ⏱ Execution time tracking
* 🔄 Session reset & state handling
* 🧩 Modular & extensible architecture

---

## 📁 Project Structure

```id="pro1"
PythonParallelTextProcessor/
│
├── app.py                # Streamlit UI application
├── main.py               # Core execution script
├── processor.py          # Processing engine
├── chunk_manager.py      # Chunk segmentation
├── sentiment_rules.py    # Sentiment logic
├── db_manager.py         # SQLite integration
├── generator.py          # Dataset generator
│
├── Dataset.csv
├── sentiment_dataset_5000.csv
├── output_results.csv
├── project.db
│
├── .streamlit/
│   └── config.toml
│
├── .gitignore
├── README.md
└── License.txt
```


## 🚀 Usage

### ▶ Run Backend Processing

```bash id="pro3"
python main.py
```

### ▶ Run Streamlit Dashboard

```bash id="pro4"
streamlit run app.py
```

---

## 🏗 Architecture

```id="pro5"
User Input
   ↓
File Upload & Validation
   ↓
Data Extraction
   ↓
Chunk Segmentation
   ↓
Parallel Processing Engine
   ↓
Sentiment Analysis
   ↓
Result Aggregation
   ↓
Dashboard Visualization
   ↓
Search / Export
```
## ⚙️ Installation Guide
**🔹 Prerequisites**
Ensure the following software is installed on your system:

* 🐍 Python 3.8 or higher
* 💾 SQLite (optional for database viewing)
* Check Python installation:

   * python --version

---
## ⚡ Processing Performance Comparison
The system evaluates three different processing approaches.

 🔹 Single Processing 
Processes reviews sequentially using one CPU core.

🔹 Thread Processing 
Uses multiple threads to process reviews concurrently.

🔹 Multiprocessing
Uses multiple CPU cores to process reviews in parallel.

The program automatically determines the fastest processing method.

**Example result:**

 Single Processing: 7.62 sec
 Thread Processing: 12.00 sec
 Multiprocessing: 1.51 sec
 Fastest Method: Multiprocessing
---


## ⚡ Workflow

1. Upload dataset
2. Validate input
3. Preview data
4. Extract text
5. Chunk segmentation
6. Parallel execution
7. Sentiment computation
8. Result aggregation
9. Visualization
10. Search & export

---
## ⚡ Parallel Processing Logic

 The system uses multiprocessing to speed up text processing.

 The dataset is divided into smaller chunks
 Each chunk is assigned to a CPU core
 All chunks are processed simultaneously
 Results are combined into a final output.
💡 Workflow
Dataset → Split into Chunks → Parallel Processing → Merge Results
🚀 Benefit
Faster execution (up to ~5x improvement)
Efficient CPU utilization
Suitable for large datasets
---

## 📦 Processing Strategy

| Dataset Size | Chunk Size | Total Chunks |
| ------------ | ---------- | ------------ |
| 50,000       | 1,000      | 50           |
| 100,000      | 10,000     | 10           |
| 1,000,000    | 10,000     | 100          |

---

## 🧠 Sentiment Engine

**Logic:**

```id="pro6"
Score = Positive Words − Negative Words
```

| Score Condition | Sentiment |
| --------------- | --------- |
| > 0             | Positive  |
| < 0             | Negative  |
| = 0             | Neutral   |

---

## 📊 Dashboard

* Total processed records
* Sentiment distribution
* CPU utilization
* Processing time

---

## 📈 Performance

| Execution Mode | Time  |
| -------------- | ----- |
| Sequential     | 7.62s |
| Parallel       | 1.51s |

🚀 **~5x faster using multiprocessing**

---

## 💾 Database

SQLite (`project.db`)

**Stored Fields:**

* id
* text
* score
* sentiment

---

## 📌 Milestones

* ✔ Data preprocessing & sentiment logic
* ✔ Parallel processing optimization
* ✔ Streamlit dashboard
* ✔ Large dataset handling

---



## 🛠 Tech Stack

| Category      | Technology      |
| ------------- | --------------- |
| Language      | Python          |
| UI            | Streamlit       |
| Data          | Pandas          |
| Visualization | Matplotlib      |
| Database      | SQLite          |
| Parallelism   | Multiprocessing |

---
## 🎯 Conclusion
This project demonstrates how large text datasets can be efficiently processed using chunk-based processing, rule-based sentiment analysis, and parallel computing techniques.It also highlights the importance of database indexing and performance benchmarking when working with large-scale data processing systems.
---

## 👩‍💻 Author

**Niharika Devi Guttula**

---

## 📜 License

This project is licensed under the MIT License.

---

<p align="center">
⭐ If you found this project useful, consider giving it a star!
</p>
