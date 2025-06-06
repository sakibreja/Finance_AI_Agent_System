# utils/rules_engine.py

import re

def validate_loan_data(text):
    """Check if loan application has required fields with basic rules."""

    findings = {}

    # Check credit score
    match = re.search(r'credit score\s*[:\-]?\s*(\d+)', text, re.I)
    if match:
        score = int(match.group(1))
        findings["credit_score"] = "PASS" if score >= 600 else f"FAIL (score = {score})"
    else:
        findings["credit_score"] = "MISSING"

    # Check annual income
    match = re.search(r'income\s*[:\-]?\s*₹?([\d,]+)', text, re.I)
    if match:
        income = int(match.group(1).replace(',', ''))
        findings["income"] = "PASS" if income >= 300000 else f"FAIL (₹{income})"
    else:
        findings["income"] = "MISSING"

    # Check for loan amount
    match = re.search(r'loan amount\s*[:\-]?\s*₹?([\d,]+)', text, re.I)
    if match:
        findings["loan_amount"] = "PRESENT"
    else:
        findings["loan_amount"] = "MISSING"

    return findings

# Payroll compliance logic

def check_payroll_compliance(gross, tax, country):
    """
    Simple compliance check:
    - In India: Income > ₹5L → Tax ≥ 10%
    """
    if country.lower() == "india" and gross >= 500000:
        expected_tax = 0.10 * gross
        return "PASS" if tax >= expected_tax else f"FAIL (Expected ≥ ₹{expected_tax:.0f})"
    return "PASS"
