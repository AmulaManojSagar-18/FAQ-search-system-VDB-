# Vector DB FAQ Search System

A simple Python project to understand:

* Embeddings
* Vector Databases
* Semantic Search
* ChromaDB

---

## Project Architecture

```text
User Question
      │
      ▼
Embedding Model
(Sentence Transformer)
      │
      ▼
Query Vector
      │
      ▼
ChromaDB Vector Search
      │
      ▼
Most Similar FAQ
      │
      ▼
Return Answer
```

---

## How Data Gets Stored

```text
FAQ Question
      │
      ▼
Embedding Model
      │
      ▼
Vector
[0.12, -0.44, 0.88 ...]
      │
      ▼
ChromaDB
```

---

## ChromaDB Collection

| ID | Question                       | Stored Vector      | Answer                                      |
| -- | ------------------------------ | ------------------ | ------------------------------------------- |
| 1  | What is Python?                | [0.12, 0.44, ...]  | Python is a programming language            |
| 2  | What is React?                 | [0.54, -0.21, ...] | React is a frontend JavaScript library      |
| 3  | Which planet is the largest?   | [0.78, 0.11, ...]  | Jupiter is the largest planet               |
| 4  | What is a virtual environment? | [0.91, -0.34, ...] | A virtual environment isolates dependencies |

---

## Install Dependencies

Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Packages

```bash
pip install chromadb sentence-transformers
```

Save Dependencies

```bash
pip freeze > requirements.txt
```

Install Dependencies Later

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python main.py
```

Example:

```text
Ask your question:
Which planet is biggest?
```

Output:

```text
Jupiter is the largest planet in our solar system.
```

---

## Technologies Used

| Component       | Technology            |
| --------------- | --------------------- |
| Language        | Python                |
| Embedding Model | all-MiniLM-L6-v2      |
| Vector Database | ChromaDB              |
| ML Framework    | Sentence Transformers |

---

## How It Works Internally

```text
Question
   ↓
Tokenizer
   ↓
Embedding Model
   ↓
384 Dimension Vector
   ↓
Stored in ChromaDB
   ↓
Similarity Search
   ↓
Best Matching Answer
```

 
