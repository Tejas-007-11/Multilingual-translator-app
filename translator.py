# translator.py
from transformers import MarianMTModel, MarianTokenizer

def load_model(src_lang: str, tgt_lang: str):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def translate(text: str, src_lang: str, tgt_lang: str):
    tokenizer, model = load_model(src_lang, tgt_lang)
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    output = tokenizer.decode(translated[0], skip_special_tokens=True)
    return output
