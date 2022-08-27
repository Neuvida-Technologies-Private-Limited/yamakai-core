import os
 
from google.cloud import translate_v2
 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/home/vishal/Desktop/yamakai-core/hindi-eng-357711-94d6f15b00c1.json"
 
translate_client = translate_v2.Client()

