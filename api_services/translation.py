import deepl
import os

# Create a Translator object providing your DeepL API authentication key.
# translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))
translator = deepl.Translator(auth_key="db5fb0cf-3283-a926-9b7a-c09c9b69bdc1:fx")

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