# doc_router.py

from llm.prompt_templates import DOC_ROUTER_PROMPT
from llm.llm_utils import call_llm

def route_document(content, llm):
    """Classify document type using LLM."""
    prompt = DOC_ROUTER_PROMPT.format(document=content)
    response = call_llm(prompt, llm)
    return response.lower().strip()
