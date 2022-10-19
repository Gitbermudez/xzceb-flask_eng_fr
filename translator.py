"""translator.py """
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
                        version='2018-05-01',
                        authenticator=authenticator
                        )
language_translator.set_service_url

#url = os.environ['url']
url = os.environ['https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/1ba4b7f1-a462-4dfd-b5af-68ad0ee6fce1']

def englishToFrench(englishText):
    """ 
    This function traslates english to french
    """
    #write the code here
    frenchtranslation = language_translator.translate(
                                text=englishText,
                                model_id='en-fr'
                            ).get_result()

    #return frenchText 
    return frenchtranslation.get("translations")[0].get("translation")

def frenchToEnglish(frenchText):
    """ 
    This function traslates english to french
    """
    #write the code here
    englishtranslation = language_translator.translate(
                            text=frenchText, model_id='en-fr'
                            ).get_result()

    #return frenchText 
    return englishtranslation.get("translations")[0].get("translation")
