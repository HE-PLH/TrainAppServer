import requests
import datetime
import base64
import json
import time
import requests
from requests.auth import HTTPBasicAuth
import mpesa.keys as keys
import mpesa.access_tk as access_tk


# get access token

consumer_key = keys.ConsumerKey
consumer_secret =keys.ConsumerSecret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
json_res=r.json()
myaccess_token=json_res['access_token']


# End get of access token

print (myaccess_token)
access_token = myaccess_token
api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
headers = {"Authorization": "Bearer %s" % myaccess_token}
request = { "ShortCode":keys.shortcode1,
  "CommandID":"CustomerPayBillOnline",
  "Amount":"1",
  "Msisdn":"254791836987",
  "BillRefNumber":"This is the ref" }

response = requests.post(api_url, json = request, headers=headers)

print (response.text)
