# 🤖 Finance AI Agent System

A modular AI agent system powered by LLMs and rules to automate analysis of financial documents like loan statements, tax forms, and mutual fund portfolios — all integrated into a Gradio web interface.

> Built by **Md Sakib Reja** | AI/ML & GenAI Developer

---

## 🧩 Features

- 🔍 **Document Router Agent** – Classifies documents automatically (Loan, Tax, Mutual Funds)
- 🏦 **Loan Verifier Agent** – Extracts EMI, loan amount, and provides LLM-based summary
- 💰 **Tax Filing Agent** – Summarizes Form-16 or tax documents
- 📊 **Mutual Fund Valuation Agent** – Calculates portfolio value from CSV + LLM reasoning
- 🌐 **Gradio Web UI** – Upload, analyze & view results from a clean browser interface
- 🔗 **Modular Design** – Easy to extend with OCR, APIs, new agents, memory, or cloud tools

---

## 👨‍💻 Author
- Md Sakib Reja
- AI/ML & GenAI Developer

## 🖼️ Architecture

┌──────────────────────────┐
│ User Interface │◄──── (Gradio)
└────────────┬─────────────┘
│
▼

┌──────────────────────────┐
│ Agent Orchestrator │◄──── (Python Logic)
└────────────┬─────────────┘

┌───────┼────────────────────────────────────────────────────┐
▼ ▼ ▼ ▼ ▼ ▼
┌────────┐ ┌────────────┐ ┌──────────────┐ ┌────────────┐ ┌────────────┐
│OCR/API │ │Loan Verifier│ │Tax Filer Agent│ │Fund Valuator│ │Doc Router │
└────────┘ └────────────┘ └──────────────┘ └────────────┘ └────────────┘
│ │ │ │ │
▼ ▼ ▼ ▼ ▼

┌────────────────────────────────────────────────────────────────────┐
│ Common Intelligence Layer (GPT-4o / Claude / Gemini via LLMs) │
└────────────────────────────────────────────────────────────────────┘
│
▼
┌──────────────────────────┐
│ Data & Knowledge Base │◄──── Spreadsheets, APIs, Vector DBs
└──────────────────────────┘
