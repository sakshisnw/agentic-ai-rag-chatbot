from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

from config import LLM_MODEL

def get_llm():
    hf_pipeline = pipeline(
        task="text2text-generation",
        model=LLM_MODEL,
        max_new_tokens=256
    )

    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    return llm
