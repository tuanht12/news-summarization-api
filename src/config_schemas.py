import pydantic


class GeneratorConfig(pydantic.BaseModel):
    # max length of generated text
    max_length: int = 256
    # early stopping
    early_stopping: bool = True
    # number of outputs
    num_return_sequences: int = 3
    # diversity_penalty = 0.0 means no penalty. The higher the penalty,
    # the more diverse are the outputs.
    diversity_penalty: float = 10.0
    # Number of beams for beam search. 1 means no beam search.
    num_beams: int = 4
    # Number of groups to divide num_beams into in order to
    # ensure diversity among different groups of beams
    num_beam_groups: int = 2


class DecodeTokenizerConfig(pydantic.BaseModel):
    skip_special_tokens: bool = True
    clean_up_tokenization_spaces: bool = True


class InferenceConfig(pydantic.BaseModel):
    generator: GeneratorConfig
    decode_tokenizer: DecodeTokenizerConfig
