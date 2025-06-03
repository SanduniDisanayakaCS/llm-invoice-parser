# 🤖 LLM-Powered Invoice Parser + Insights

A Streamlit-based AI app that extracts structured data from PDF invoices using LLMs and generates clean summaries — perfect for freelancers, businesses, and financial tools.

---

## 🚀 Features

- 📤 Upload scanned or digital PDF invoices
- 📄 Extract text using PDF parsing (pdfplumber)
- 🧠 Analyze invoice data using OpenAI GPT
- 📊 Automatically generate:
  - Invoice number
  - Date
  - Total amount
  - Itemized details
  - Due date
  - Monthly summary
- ⚡ Fast and interactive UI via Streamlit

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Backend Logic**: Python + OpenAI (GPT-3.5)
- **PDF Parsing**: `pdfplumber`
- **Secrets Management**: `.env` file + `python-dotenv`

---

## 🧪 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/YourUsername/llm-invoice-parser.git
cd llm-invoice-parser

2. Install Requirements

pip install -r requirements.txt

3. Setup API Key
Create a .env file:

OPENAI_API_KEY=your-api-key-here

4. Launch App
streamlit run app.py

📁 Folder Structure

llm-invoice-parser/
├── app.py
├── parser.py
├── insights.py
├── requirements.txt
├── .env
└── sample_invoice.pdf

📌 Use Cases
Freelancers managing client invoices

Startups building AI financial tools

Automation of manual invoice processing

Demo for LLM prompt engineering and integration

⭐ Future Ideas
 Convert output to JSON or Excel

 Add charts (monthly spending)

 Upload multiple invoices