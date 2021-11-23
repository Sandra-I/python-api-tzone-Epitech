import deepl
import os

# Create a Translator object providing your DeepL API authentication key.
# To avoid writing your key in source code, you can set it in an environment
# variable DEEPL_AUTH_KEY, then read the variable in your Python code:
# translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))

translator = deepl.Translator(auth_key)

def translation_text(text, target_lang):
    # Translate text into a target language, in this case, French
    result = translator.translate_text(text, target_lang=target_lang)
    result.target_lang = "FR"
    return result