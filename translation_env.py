import os
import requests, uuid, json
from google.cloud import translate_v2
from google.cloud import translate
import boto3
 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/home/vishal/Desktop/yamakai-core/hindi-eng-357711-94d6f15b00c1.json"
 
translate_client = translate_v2.Client()

client = translate.TranslationServiceClient()

## AWS Translate

translate = boto3.client(service_name='translate', region_name='ap-south-1', use_ssl=True)

result = translate.translate_text(Text="1. Renegade is the best platform to buy premium self-care and grooming products for men online. \n \
        2. We feature all the top brands as well as upcoming brands that are gaining market traction. \n \
        3. We provide a convenient platform for men to shop for all their self-care and grooming needs in one place. \n \
        4. Our products are carefully curated and chosen for their quality, functionality, and style. \n \
        5. We offer free shipping on orders over $100 and easy returns so you can shop with confidence. \n \
        6. For more information, please visit our website at www.renegadegroomingco.com or contact us at info@renegadegroomingco", 
            SourceLanguageCode="en", TargetLanguageCode="de")
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))

## Mircrosoft translate

key = "get-it-from-azure"
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "centralindia"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['fr']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text':"""1. Renegade is the best platform to buy premium self-care and grooming products for men online. 
              2. We feature all the top brands as well as upcoming brands that are gaining market traction.
              3. We provide a convenient platform for men to shop for all their self-care and grooming needs in one place. 
              4. Our products are carefully curated and chosen for their quality, functionality, and style.
              5. We offer free shipping on orders over $100 and easy returns so you can shop with confidence.
              6. For more information, please visit our website at www.renegadegroomingco.com or contact us at info@renegadegroomingco"""
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(response[0].get('translations')[0].get('text'))