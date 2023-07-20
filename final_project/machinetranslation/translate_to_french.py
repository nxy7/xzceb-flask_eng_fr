"""Translation module."""

from deep_translator import MyMemoryTranslator

def english_to_french(translation_text) -> str:
    """
        Translates text from english to french
    """
    ret_str = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(translation_text)
    return ret_str
