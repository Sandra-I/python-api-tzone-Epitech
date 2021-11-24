import deepl
import os

# Create a Translator object providing your DeepL API authentication key.
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))

def translation_text(text, target_lang):
    result = None
    if text:
        try:
            result = translator.translate_text(text, target_lang=target_lang)
        except deepl.DeepLException as err:
            raise err

    if result:
        result.target_lang = target_lang
        return result