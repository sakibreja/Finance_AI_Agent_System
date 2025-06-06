# components/payroll_checker.py

import pandas as pd
from utils.rules_engine import check_payroll_compliance
from llm.prompt_templates import PAYROLL_LLM_ANALYSIS_PROMPT
from llm.llm_utils import call_llm

def reconcile_payroll(file_path, llm):
    """Reconcile payroll entries and return anomalies + LLM analysis."""

    df = pd.read_csv(file_path)
    results = []

    for _, row in df.iterrows():
        emp_id = row["Employee ID"]
        gross = row["Gross Salary"]
        tax = row["Tax Deducted"]
        net = row["Net Pay"]
        country = row.get("Country", "India")

        # Step 1: Arithmetic Check
        net_calc = gross - tax
        net_status = "PASS" if abs(net - net_calc) < 1 else f"FAIL (Expected: {net_calc})"

        # Step 2: Tax Compliance
        tax_check = check_payroll_compliance(gross, tax, country)

        # Step 3: LLM Explanation
        llm_prompt = PAYROLL_LLM_ANALYSIS_PROMPT.format(
            emp_id=emp_id, gross=gross, tax=tax, net=net, country=country
        )
        llm_response = call_llm(llm_prompt, llm)

        results.append({
            "Employee ID": emp_id,
            "Net Pay Check": net_status,
            "Tax Compliance": tax_check,
            "LLM Review": llm_response
        })

    return results
