# 📄 Contract Clause Extraction & Analysis Engine

## 🚀 Overview
This project is a Django-based system that extracts, analyzes, and queries legal clauses from commercial contracts using the CUAD dataset.

It enables:
- Clause extraction by category
- Question answering over contracts
- Source traceability (context + location)
- Dynamic query handling without hardcoded categories

---

## 🏗️ Architecture
            +----------------------+
            |   CUAD Dataset       |
            | (JSON contracts)     |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |   Ingestion Layer    |
            |  (Parsing + Storage) |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |   Django Models      |
            | Contract / Clause   |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |   QA Engine          |
            | (Dynamic Matching)   |
            +----------+-----------+
                       |
                       v
            +----------------------+
            |   REST APIs          |
            | Upload / Ask / View  |
            +----------------------+


---

## ⚙️ Setup Instructions

### 1️⃣ Clone repo
```bash
git clone <your-repo-link>
cd contract_analyzer
2️⃣ Create virtual environment
python -m venv venv
```venv\Scripts\activate   # Windows
```
3️⃣ Install dependencies
```pip install -r requirements.txt
```
pip install -r requirements.txt
```python manage.py makemigrations
python manage.py migrate
```
5️⃣ Run server
```python manage.py runserver```
5️⃣ Run server
```python manage.py runserver
```
📂 Dataset Setup
Download CUAD dataset:
https://github.com/TheAtticusProject/cuad
Extract:
data/train_separate_questions.json
Place inside project:
contract_analyzer/data/
📥 Ingest Data
python manage.py shell
from contracts.services.ingestion import ingest_cuad_contracts
ingest_cuad_contracts(limit=20)
🔗 API Endpoints
1️⃣ List Contracts
GET /contracts/
2️⃣ Get Clauses
GET /contracts/<id>/clauses/
3️⃣ Ask Question (Contract-specific)
POST /contracts/<id>/ask/

Body:

{
  "question": "What is the governing law?"
}
📂 Dataset Setup
Download CUAD dataset:
https://github.com/TheAtticusProject/cuad
Extract:
data/train_separate_questions.json
Place inside project:
contract_analyzer/data/
📥 Ingest Data
python manage.py shell
from contracts.services.ingestion import ingest_cuad_contracts
ingest_cuad_contracts(limit=20)
🔗 API Endpoints
1️⃣ List Contracts
GET /contracts/
2️⃣ Get Clauses
GET /contracts/<id>/clauses/
3️⃣ Ask Question (Contract-specific)
POST /contracts/<id>/ask/

Body:

{
  "question": "What is the governing law?"
}