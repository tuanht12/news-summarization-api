from loguru import logger
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from configs.conf import HUGGINGFACE_MODEL_ID, MODEL_DIR


def download_pretrained_model():
    # Check if the model is already downloaded
    if not MODEL_DIR.exists():
        model = AutoModelForSeq2SeqLM.from_pretrained(HUGGINGFACE_MODEL_ID)
        tokenizer = AutoTokenizer.from_pretrained(HUGGINGFACE_MODEL_ID)
        model.save_pretrained(MODEL_DIR)
        tokenizer.save_pretrained(MODEL_DIR)
        logger.info(f"Model and tokenizer are saved to {MODEL_DIR}")


if __name__ == "__main__":
    download_pretrained_model()
