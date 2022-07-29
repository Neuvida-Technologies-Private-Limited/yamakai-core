import os
 
from google.cloud import translate_v2
 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/home/vishal/Desktop/yamakai-core/hindi-eng-357711-54aa0aff4660.json"
 
translate_client = translate_v2.Client()

