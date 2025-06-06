# components/tax_filer.py

import re
from llm.prompt_templates import TAX_AGENT_PROMPT
from llm.llm_utils import call_llm

def extract_tax_fields(text):
    """Use regex to extract key tax fields from the document."""
    fields = {}

    patterns = {
        "name": r"Name[:\-]?\s*(.+)",
        "pan": r"PAN[:\-]?\s*([A-Z]{5}\d{4}[A-Z])",
        "salary": r"Salary Income[:\-]?\s*₹?([\d,]+)",
        "rental": r"Rental Income[:\-]?\s*₹?([\d,]+)",
        "other": r"Other Income[:\-]?\s*₹?([\d,]+)",
        "ded_80c": r"Deductions \(80C\)[:\-]?\s*₹?([\d,]+)",
        "ded_80d": r"Deductions \(80D\)[:\-]?\s*₹?([\d,]+)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.I)
        if match:
            fields[key] = match.group(1).replace(',', '').strip()
        else:
            fields[key] = "0"

    return fields

def compute_taxable_income(fields):
    income = sum([
        int(fields.get("salary", 0)),
        int(fields.get("rental", 0)),
        int(fields.get("other", 0)),
    ])
    deductions = sum([
        int(fields.get("ded_80c", 0)),
        int(fields.get("ded_80d", 0))
    ])
    taxable = max(income - deductions, 0)
    return income, deductions, taxable

def tax_filing_agent(document_text, llm):
    fields = extract_tax_fields(document_text)
    total_income, total_deductions, taxable_income = compute_taxable_income(fields)

    llm_result = call_llm(
        TAX_AGENT_PROMPT.format(
            name=fields.get("name", "Taxpayer"),
            pan=fields.get("pan", "UNKNOWN"),
            income=total_income,
            deductions=total_deductions,
            taxable=taxable_income
        ),
        llm
    )

    return {
        "Extracted Fields": fields,
        "Total Income": total_income,
        "Total Deductions": total_deductions,
        "Taxable Income": taxable_income,
        "LLM Filing Advice": llm_result
    }
