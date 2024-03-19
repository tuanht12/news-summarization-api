import regex as re
import yaml
from loguru import logger
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from configs.conf import MODEL_DIR
from src.config_schemas import InferenceConfig


class TextSummarizer:
    def __init__(self, inference_config_path: str) -> None:
        self.inference_config_path = inference_config_path
        self.inference_config = self._get_inference_config()
        self.generator_config = self.inference_config.generator.dict()
        self.decode_tokenizer_config = self.inference_config.decode_tokenizer.dict()
        self._init_model()

    def _get_inference_config(self) -> InferenceConfig:
        with open(self.inference_config_path, "r") as file:
            inference_config = yaml.safe_load(file)
        return InferenceConfig(**inference_config)

    def _init_model(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)

    @staticmethod
    def _add_prefix_suffix(text: str) -> str:
        prefix = "vietnews: "
        suffix = " </s>"
        return prefix + text + suffix

    @staticmethod
    def _preprocess_text(text: str) -> str:
        """
        Clean the text by removing special characters, extra spaces, etc.

        Args:
            text (str): The text to clean.

        Returns:
            str: The cleaned text.
        """
        # remove leading and trailing whitespace
        text = text.strip()

        # remove redundant spaces
        text = re.sub(r" {2,}", " ", text)

        # remove redundant newlines
        text = re.sub(r"\n{2,}", "\n", text)

        # remove special characters
        text = re.sub(r"[^\p{L}\p{N}\p{M}\s\p{P}]", "", text)

        return text

    def _prepare_input(self, text: str):
        assert isinstance(text, str), "Input must be a string."
        preprocessed_text = self._preprocess_text(text)
        input_text = self._add_prefix_suffix(preprocessed_text)
        input_text = self.tokenizer(
            input_text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=1024,
        )
        logger.info("Successfully prepared input for summarization.")
        return input_text

    def _generate_output_token(self, encoded_prompts: dict):
        self.model.eval()
        input_ids = encoded_prompts["input_ids"]
        attention_masks = encoded_prompts["attention_mask"]
        outputs = self.model.generate(
            input_ids=input_ids,
            attention_mask=attention_masks,
            **self.generator_config,
        )
        logger.info("Successfully generated output token.")
        return outputs

    def _decode_output(self, output_token):
        decoded_output = self.tokenizer.decode(
            output_token[0], **self.decode_tokenizer_config
        )
        logger.info("Successfully decoded final summary.")
        return decoded_output

    def summarize(self, text: str) -> str:
        encoded_prompts = self._prepare_input(text)
        output_token = self._generate_output_token(encoded_prompts)
        summary = self._decode_output(output_token)
        return summary
