import datetime
import base64
import json
import time
import requests
from requests.auth import HTTPBasicAuth
import mpesa.keys as keys
import mpesa.access_tk as access_tk
#print(datetime.datetime.now())

# get access token
myaccess_token=""

def generateToken():
    consumer_key = keys.ConsumerKey
    consumer_secret =keys.ConsumerSecret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_res=r.json()
    myaccess_token=json_res['access_token']


# End get of access token



unformated_time=datetime.datetime.now()
formatted_time=unformated_time.strftime("%Y%m%d%H%M%S")

#print(formatted_time)

#generating a time stamp

#base 64
data_to_encode=keys.businessShortCode + keys.lipa_na_mpesa_passkey + formatted_time
encoded_string=base64.b64encode(data_to_encode.encode())

decoded_pass=encoded_string.decode('utf8')

#print (decoded_pass)




#print(myaccess_token)

    #print (r.json())


def lipa_na_mpesa(phone_no='254791836987',amount='1',payBill='174379'):
    consumer_key = keys.ConsumerKey
    consumer_secret =keys.ConsumerSecret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_res=r.json()
    myaccess_token=json_res['access_token']
    access_token = myaccess_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": payBill,
    "Password": decoded_pass,
    "Timestamp":formatted_time,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": amount,
    "PartyA": phone_no,
    "PartyB":keys.partB,  
    "PhoneNumber": phone_no,  
    "CallBackURL": "http://159.65.136.22/lnmpOnline/",  
    "AccountReference": "122111",
    "TransactionDesc": "fee payment"
    }

    time.sleep(1)

    response = requests.post(api_url, json = request, headers=headers)

    # print ("This is the response",response.text)
    parsed_data = json.loads(response.text)
    print (response.text)
    print ("The response code =",parsed_data['ResponseCode'])
    ResponseCode=parsed_data['ResponseCode']
    return ResponseCode

#generate_token()

# lipa_na_mpesa()
x=lipa_na_mpesa()
# print(lipa_na_mpesa)
print (x.ResponseCode)
"""

{'Body': {'stkCallback': {'MerchantRequestID': '23481-4888433-1', 'CheckoutRequestID': 'ws_CO_DMZ_384585971_04072019121246169', 'ResultCode': 0, 'ResultDesc': 'The service request is processed successfully.', 'CallbackMetadata': {'Item': [{'Name': 'Amount', 'Value': 1.0}, {'Name': 'MpesaReceiptNumber', 'Value': 'NG421NVTR6'}, {'Name': 'Balance'}, {'Name': 'TransactionDate', 'Value': 20190704121251}, {'Name': 'PhoneNumber', 'Value': 254791836987}]}}}} 

"""




