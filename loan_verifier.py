# components/loan_verifier.py

from llm.prompt_templates import LOAN_VERIFICATION_PROMPT
from llm.llm_utils import call_llm
from utils.rules_engine import validate_loan_data

def verify_loan_application(document_text, llm):
    """Main agent to verify loan application."""
    
    # Step 1: Rule-based validation
    validation_result = validate_loan_data(document_text)

    # Step 2: LLM-based evaluation of loan manager's judgment
    llm_result = call_llm(
        LOAN_VERIFICATION_PROMPT.format(document=document_text), llm
    )

    # Step 3: Compile response
    return {
        "rule_check": validation_result,
        "llm_review": llm_result
    }
