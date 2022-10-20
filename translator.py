"""translator.py """
import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
#url = os.environ['url']
url = os.environ['https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/1ba4b7f1-a462-4dfd-b5af-68ad0ee6fce1']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url
language_translator.set_disable_ssl_verification(True)

def english_to_french(englishText):
    """ 
    This function traslates english to french
    """
    #write the code here
    frenchtranslation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    frenchText=frenchtranslation.get("translations")[0].get("translation")
    return frenchText 

def french_to_english(frenchText):
    """ 
    This function traslates english to french
    """
    #write the code here
    englishtranslation = language_translator.translate(
    text=frenchText, model_id='en-fr').get_result()
    englishText=englishtranslation.get("translations")[0].get("translation")
    return englishText 