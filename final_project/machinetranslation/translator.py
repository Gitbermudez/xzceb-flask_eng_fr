"""
translator.py
"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#from dotenv import load_dotenv
#load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
#apikey = "DYl4fdske7WTuUZc6Rl-UOmseVMzI1KLv8nW8MnyhOak"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def en_to_fr(english_text):
    """
    This function traslates english to french
    """
    #write the code here
    frenchtranslation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()

    return frenchtranslation.get("translations")[0].get("translation")
    #return french_text

def fr_to_en(french_text):
    """
    This function traslates english to french
    """
    #write the code here
    englishtranslation = language_translator.translate(
    text=french_text, model_id='fr-en').get_result()
    return englishtranslation.get("translations")[0].get("translation")
    #return english_text
    