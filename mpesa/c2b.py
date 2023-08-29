import requests
import keys
from requests.auth import HTTPBasicAuth


consumer_key = keys.ConsumerKey
consumer_secret =keys.ConsumerSecret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
json_res=r.json()
myaccess_token=json_res['access_token']

#print(myaccess_token)

def registerUrl():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % myaccess_token}
    request = { 
        "ShortCode": keys.shortcode1,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://fullstack.com/myLMP",
        "ValidationURL": "https://fullstack.com/myLMPpp"}

    response = requests.post(api_url, json = request, headers=headers)
    print (response.text)

registerUrl()
