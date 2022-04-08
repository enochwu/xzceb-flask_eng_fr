"""
Translation module for the requested English to french translation.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version_lt = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version_lt,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Function which translates English to French
    """
    translation_response = language_translator.translate(
        text=english_text, model_id='en-fr')

    translation = translation_response.get_result()

    french_text = translation['translations'][0]['translation']
    # print(f"The French translation for '{english_text}' is '{french_text}'")

    return french_text


def french_to_english(french_text):
    """
    Function which translates English to French
    """
    translation_response = language_translator.translate(
        text=french_text, model_id='fr-en')

    translation = translation_response.get_result()

    english_text = translation['translations'][0]['translation']
    # print(f"The English translation for '{french_text}' is '{english_text}'\n")

    return english_text
