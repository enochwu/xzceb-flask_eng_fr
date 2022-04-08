from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(textToTranslate)
    # Write your code here
    return f"'{textToTranslate}' was translated to French as '{translated_text}'."


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(textToTranslate)
    return f"'{textToTranslate}' was translated to English as '{translated_text}'."


@app.route("/")
def renderIndexPage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)


# @app.route("/spanishToEnglish")
# def spanishToEnglish():
#     textToTranslate = request.args.get('textToTranslate')
#
#     return "Translated text to English"
