"""
translator.py
"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
#apikey = "DYl4fdske7WTuUZc6Rl-UOmseVMzI1KLv8nW8MnyhOak"
authenticator = IAMAuthenticator('_RtomCmW3LrrujUnNKRVeQYk_9ewz1QP6Fctcvxi9cxg')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/1ba4b7f1-a462-4dfd-b5af-68ad0ee6fce1')
#language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def e2f(englishtext):
    """
    conver englist to french
    """
    translation= language_translator.translate(text=englishtext, model_id='en-fr').get_result()
    frenchtext=translation['translations'][0]['translation']
    return frenchtext

def f2e(frenchtext):
    """
    conver french to english
    """
    translation= language_translator.translate(text=frenchtext, model_id='fr-en').get_result()
    englishtext=translation['translations'][0]['translation']
    return englishtext
    