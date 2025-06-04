# finance_ai_agents
/finance_ai_agents/
│
├── main_orchestrator.ipynb         # 🔁 Main entry notebook (agent routing)
├── components/
│   ├── ocr_api_module.py           # 🧾 OCR or API input processor
│   ├── loan_verifier.py            # 🏦 Loan application verification agent
│   ├── payroll_checker.py          # 💰 Payroll reconciliation agent
│   ├── tax_filer.py                # 🧾 Tax filing agent
│   ├── fund_valuator.py           # 📊 Mutual fund valuation agent
│   └── doc_router.py              # 📑 Document classifier/router
│
├── llm/
│   ├── prompt_templates.py         # 💬 Prompt templates for LLMs
│   └── llm_utils.py                # 🧠 Wrapper for GPT-4o or Azure OpenAI
│
├── data/
│   ├── sample_inputs/              # Sample PDFs, CSVs, JSON
│   └── outputs/                    # Generated outputs or logs
│
└── utils/
    ├── vector_store.py            # 🧠 FAISS/Chroma logic
    ├── rules_engine.py            # ✅ Business validation logic
    └── file_utils.py              # 📂 File processing utilities
