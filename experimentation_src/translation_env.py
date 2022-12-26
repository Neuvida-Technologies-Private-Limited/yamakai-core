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

result = translate.translate_text(Text="""Metallurgy is a domain of materials science and engineering 
that studies the physical and chemical behavior of metallic
elements, their inter-metallic compounds, and their mixtures,
which are known as alloys. Metallurgy encompasses both 
the science and the technology of metals; that is, the way in 
which science is applied to the production of metals, and the 
engineering of metal components used in products for both 
consumers and manufacturers. Metallurgy is distinct from 
the craft of metalworking. Metalworking relies on metallurgy 
in a similar manner to how medicine relies on medical science
for technical advancement. A specialist practitioner of 
metallurgy is known as a metallurgist.""", 
            SourceLanguageCode="en", TargetLanguageCode="sk")
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))

# ## Mircrosoft translate

key = "b5c62ef73ffa43d88fe085eef093e44c"
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "centralindia"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['sk']
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
    'text':"""Metallurgy is a domain of materials science and engineering 
that studies the physical and chemical behavior of metallic
elements, their inter-metallic compounds, and their mixtures,
which are known as alloys. Metallurgy encompasses both 
the science and the technology of metals; that is, the way in 
which science is applied to the production of metals, and the 
engineering of metal components used in products for both 
consumers and manufacturers. Metallurgy is distinct from 
the craft of metalworking. Metalworking relies on metallurgy 
in a similar manner to how medicine relies on medical science
for technical advancement. A specialist practitioner of 
metallurgy is known as a metallurgist."""
    }]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(response[0].get('translations')[0].get('text'))
