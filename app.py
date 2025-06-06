# app.py

import gradio as gr
from components.document_router import route_document
from components.loan_verifier import analyze_loan_document
from components.tax_filer import analyze_tax_form
from components.fund_valuator import analyze_mutual_fund_portfolio
from llm.llm_utils import load_llm

# Load the LLM globally
llm = load_llm()

def process_file(file):
    import os

    file_path = file.name
    ext = os.path.splitext(file_path)[1]

    # Use raw text if it's a .txt file
    if ext == ".txt":
        with open(file_path, "r") as f:
            raw_text = f.read()
    elif ext == ".csv":
        raw_text = open(file_path, "r").read()  # for MF CSV
    else:
        return "Unsupported file type.", "", ""

    routing_result = route_document(raw_text, llm)
    doc_type = routing_result["document_type"]

    if doc_type == "loan_document":
        result = analyze_loan_document(raw_text, llm)
        display = f"EMI: ₹{result['EMI']:.2f}, Sanctioned: ₹{result['Sanctioned Amount']}, LLM Summary:\n{result['LLM Summary']}"
    elif doc_type == "tax_form":
        result = analyze_tax_form(raw_text, llm)
        display = f"LLM Summary:\n{result['LLM Summary']}"
    elif doc_type == "mutual_fund_portfolio":
        temp_path = "/tmp/fund.csv"
        with open(temp_path, "w") as f:
            f.write(raw_text)
        result = analyze_mutual_fund_portfolio(temp_path, llm)
        display = f"Invested: ₹{result['Total Invested']:.0f}, Current: ₹{result['Current Value']:.0f}\nLLM Summary:\n{result['LLM Summary']}"
    else:
        display = f"Unknown document type."

    return doc_type, routing_result["method"], display

with gr.Blocks(title="Finance AI Agent Dashboard") as demo:
    gr.Markdown("# 🤖 Finance AI Agent\nUpload a document (loan, tax, or mutual fund CSV)")

    with gr.Row():
        file_input = gr.File(label="Upload Document (.txt or .csv)")
        submit_btn = gr.Button("Analyze")

    with gr.Row():
        doc_type_out = gr.Textbox(label="Detected Document Type")
        routing_out = gr.Textbox(label="Routing Method (Rule/LLM)")
        output_box = gr.Textbox(label="Analysis Result", lines=10)

    submit_btn.click(fn=process_file, inputs=[file_input], outputs=[doc_type_out, routing_out, output_box])

if __name__ == "__main__":
    demo.launch()
