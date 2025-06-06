# components/fund_valuator.py

import pandas as pd
from datetime import datetime
from llm.llm_utils import call_llm
from llm.prompt_templates import FUND_VALUATION_PROMPT

def calculate_cagr(initial_value, final_value, years):
    if years <= 0 or initial_value <= 0:
        return 0
    return ((final_value / initial_value) ** (1 / years)) - 1

def analyze_mutual_fund_portfolio(file_path, llm):
    df = pd.read_csv(file_path)
    today = datetime.today()

    analysis = []
    total_value = 0
    total_invested = 0

    for _, row in df.iterrows():
        name = row["Fund Name"]
        units = float(row["Units Held"])
        nav = float(row["NAV"])
        buy_nav = float(row["Purchase NAV"])
        date = datetime.strptime(row["Purchase Date"], "%Y-%m-%d")

        current_value = units * nav
        invested_amount = units * buy_nav
        duration = (today - date).days / 365.25
        cagr = calculate_cagr(invested_amount, current_value, duration)

        total_value += current_value
        total_invested += invested_amount

        analysis.append({
            "Fund Name": name,
            "Current Value": current_value,
            "Invested": invested_amount,
            "CAGR": round(cagr * 100, 2),
            "Years Held": round(duration, 2)
        })

    # Format LLM summary
    llm_input = "\n".join([
        f"{a['Fund Name']}: Invested ₹{a['Invested']:.0f}, Value ₹{a['Current Value']:.0f}, CAGR {a['CAGR']}%"
        for a in analysis
    ])

    llm_summary = call_llm(FUND_VALUATION_PROMPT.format(
        summary_text=llm_input,
        total_invested=int(total_invested),
        total_value=int(total_value)
    ), llm)

    return {
        "Fund Analysis": analysis,
        "Total Invested": total_invested,
        "Current Value": total_value,
        "LLM Summary": llm_summary
    }
