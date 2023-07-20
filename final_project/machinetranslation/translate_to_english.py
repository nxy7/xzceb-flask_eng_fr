"""Translation module."""

from deep_translator import MyMemoryTranslator

def french_to_english(translation_text) -> str:
    """
        Translates text from french to english
    """
    ret_str = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(translation_text)
    return ret_str
