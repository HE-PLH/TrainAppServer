import mpesa.keys as keys

import requests
from requests.auth import HTTPBasicAuth


consumer_key = keys.ConsumerKey
consumer_secret =keys.ConsumerSecret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
json_res=r.json()
myaccess_token=json_res['access_token']