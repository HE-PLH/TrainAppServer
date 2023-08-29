import requests
import datetime
import base64
import json
import time
import requests
from requests.auth import HTTPBasicAuth
import mpesa.keys as keys
import mpesa.access_tk as access_tk


def registerUrl():
    consumer_key = keys.ConsumerKey
    consumer_secret =keys.ConsumerSecret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_res=r.json()
    myaccess_token=json_res['access_token']

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % myaccess_token}
    request = { "ShortCode": keys.shortcode1,
        "ResponseType": "Completed",
        "ConfirmationURL": "http://159.65.136.22/lnmp",
        "ValidationURL": "http://159.65.136.22/lnmpOnline"}

    response = requests.post(api_url, json = request, headers=headers)

    print ("This is the response: ", response.text)

    return myaccess_token;


x=registerUrl()
print(x)