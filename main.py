from fastapi import FastAPI

from configs.conf import INFERENCE_CONFIG_PATH
from src.text_summarizer import TextSummarizer

app = FastAPI()

text_summarizer = TextSummarizer(INFERENCE_CONFIG_PATH)


@app.post("/summarize")
def summarize(text: str):
    summary = text_summarizer.summarize(text)
    return {"summary": summary}
