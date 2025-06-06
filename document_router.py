# components/document_router.py

from llm.llm_utils import call_llm
from llm.prompt_templates import DOC_ROUTER_PROMPT

def simple_keyword_classifier(text):
    text_lower = text.lower()

    if "loan amount" in text_lower or "emi" in text_lower:
        return "loan_document"
    elif "form 16" in text_lower or "income tax" in text_lower:
        return "tax_form"
    elif "fund name" in text_lower or "nav" in text_lower:
        return "mutual_fund_portfolio"
    elif "salary" in text_lower and "payslip" in text_lower:
        return "payroll_document"
    else:
        return None

def route_document(text, llm):
    rule_based_type = simple_keyword_classifier(text)
    
    if rule_based_type:
        return {
            "method": "rule_based",
            "document_type": rule_based_type
        }

    # Fallback to LLM
    doc_type = call_llm(DOC_ROUTER_PROMPT.format(text=text), llm)
    return {
        "method": "llm",
        "document_type": doc_type.strip().lower()
    }
# This function first checks for specific keywords to classify the document type.