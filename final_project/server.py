from machinetranslation import translate_to_english, translate_to_french
from flask import Flask, request
# from translate_to_english import FrenchToEnglish
# from translate_to_french import EnglishToFrench
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return translate_to_english.french_to_english(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return translate_to_french.english_to_french(textToTranslate)

@app.route("/")
def renderIndexPage():
    return "Ok"
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
