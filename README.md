# 🚀 Parallel Text Processing & Sentiment Analysis System

A Python-based system designed to **analyze large text datasets efficiently** using **chunk-based processing, rule-based sentiment detection, and parallel execution techniques**.

The system evaluates **different processing approaches (Single, Thread, and Multiprocessing)** while storing results in a **SQLite database** and analyzing **query performance improvements through indexing**.

---

# 📌 Project Highlights

✨ Efficient processing of large text datasets
✨ Rule-based sentiment analysis engine
✨ Chunk-based scalable processing
✨ Performance benchmarking (Single vs Thread vs Multiprocessing)
✨ SQLite database storage
✨ Query optimization using indexing
✨ Sentiment distribution analysis

---

# 📁 Project Structure

```
PythonParallelTextProcessor/
│
├── main.py               # 🚦 Main execution script
├── chunk_manager.py     # 📦 Dataset loading & chunk creation
├── sentiment_rules.py   # 🧠 Rule-based sentiment analysis engine
├── db_manager.py        # 💾 SQLite database operations
├── generator.py         # 🧪 Synthetic dataset generator
├── Dataset.csv          # 📄 Input dataset containing reviews
├── project.db           # 🗄 SQLite database (auto-generated)
└── README.md            # 📘 Project documentation
```

---

# ⚙️ Installation Guide

## 🔹 Prerequisites

Ensure the following software is installed on your system:

* 🐍 **Python 3.8 or higher**
* 💾 **SQLite (optional for database viewing)**

Check Python installation:

```bash
   python --version
```
---

# 🔄 System Workflow

```
📄 Dataset.csv
      ↓
📥 Load Dataset
      ↓
📦 Create Chunks
      ↓
🧹 Clean Text
      ↓
🧠 Sentiment Analysis
      ↓
⚡ Performance Comparison
      ↓
💾 Store Results in Database
      ↓
📊 Query Optimization
```

---

# 📦 Chunk Processing

Large datasets are divided into smaller units called **chunks** to improve efficiency.

Example:

Dataset Size

```
60000 rows
```

Chunk Size

```
1000 rows
```

Total Chunks

```
60000 ÷ 1000 = 60 chunks
```

Each chunk contains **1000 reviews**, allowing the system to process large datasets more efficiently.

---

# 🧠 Sentiment Analysis Method

The project uses a **Rule-Based Sentiment Analysis** approach.

Two predefined word lists determine sentiment.

### ✅ Positive Words

```
good
great
excellent
happy
```

### ❌ Negative Words

```
bad
terrible
worst
```

### 📊 Sentiment Score Formula

```
Sentiment Score = Positive Words − Negative Words
```

### 🏷 Sentiment Classification

| Score | Sentiment |
| ----- | --------- |
| > 0   | Positive  |
| < 0   | Negative  |
| = 0   | Neutral   |

### Example

Review:

```
this product is great
```

Detected Word:

```
great → positive
```

Result:

```
Score: 1
Sentiment: Positive
```

---

# ⚡ Processing Performance Comparison

The system evaluates three different processing approaches.

### 🔹 Single Processing

Processes reviews sequentially using **one CPU core**.

### 🔹 Thread Processing

Uses **multiple threads** to process reviews concurrently.

### 🔹 Multiprocessing

Uses **multiple CPU cores** to process reviews in parallel.

The program automatically determines the **fastest processing method**.

Example result:

```
Single Processing: 7.62 sec
Thread Processing: 12.00 sec
Multiprocessing: 1.51 sec
Fastest Method: Multiprocessing
```

---

# 📊 Sentiment Distribution

After processing all reviews, the system calculates the distribution of sentiments.

Example output:

```
Positive : 26749 (44.6%)
Negative : 26458 (44.1%)
Neutral  : 6793 (11.3%)
```

This helps understand the **overall sentiment trend of the dataset**.

---

# 💾 Database Storage

All processed results are stored in a **SQLite database**.

Database File:

```
project.db
```

### Database Table Structure

| id | text | score | sentiment |
| -- | ---- | ----- | --------- |

Example Record:

| id | text                        | score | sentiment |
| -- | --------------------------- | ----- | --------- |
| 1  | this product is really good | 1     | Positive  |

---

# ⚡ Query Optimization

The project evaluates database query performance before and after indexing.

Example:

```
Query Before Index: 0.173 sec
Query After Index: 0.154 sec
Index Improvement: 1.15X Faster
```

Indexes improve **database search speed**, especially for large datasets.

---

# 📈 Example Program Output

```
Loading dataset...
Total Records: 60000

Chunk Processing Result
-----------------------
Total rows: 60000
Total chunks: 60

Processing Performance
-----------------------
Single Processing: 7.62 sec
Thread Processing: 12.00 sec
Multiprocessing: 1.51 sec
Fastest Method: Multiprocessing

Sentiment Distribution
-----------------------
Positive : 26749 (44.6 %)
Negative : 26458 (44.1 %)
Neutral  : 6793 (11.3 %)

Database Performance
-----------------------
Bulk Insert Time: 0.591 sec
Query Before Index: 0.173 sec
Query After Index: 0.154 sec

Project Execution Completed Successfully
```

---

# 📌 Project Milestones

## 🟢 Milestone 1

Implemented:

✔ Dataset loading
✔ Text preprocessing
✔ Rule-based sentiment analysis
✔ Chunk-based processing
✔ Database storage
✔ Query optimization

---

## 🟢 Milestone 2

Added:

✔ Parallel processing comparison
✔ ThreadPool execution
✔ Multiprocessing execution
✔ Performance benchmarking
✔ Scalability observation

---

# 🛠 Technologies Used

🐍 Python
💾 SQLite
📄 CSV File Processing
⚡ Parallel Computing (Threading & Multiprocessing)
🧠 Rule-Based NLP

---

# 🎯 Conclusion

This project demonstrates how large text datasets can be efficiently processed using **chunk-based processing, rule-based sentiment analysis, and parallel computing techniques**.

It also highlights the importance of **database indexing and performance benchmarking** when working with large-scale data processing systems.
