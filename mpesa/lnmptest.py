import datetime
import base64
import requests
from requests.auth import HTTPBasicAuth
import mpesa.keys as keys
import mpesa.access_tk as access_tk
#print(datetime.datetime.now())

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


def lipa_na_mpesa(phone_no='254791836987'):
    access_token = access_tk.myaccess_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": keys.businessShortCode,
    "Password": decoded_pass,
    "Timestamp":formatted_time,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": phone_no,
    "PartyB":keys.partB,  
    "PhoneNumber": phone_no,  
    "CallBackURL": "http://159.65.136.22/lnmp/",  
    "AccountReference": "122111",
    "TransactionDesc": "fee payment"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

#generate_token()

lipa_na_mpesa()


# """

# {'Body': {'stkCallback': {'MerchantRequestID': '23481-4888433-1', 'CheckoutRequestID': 'ws_CO_DMZ_384585971_04072019121246169', 'ResultCode': 0, 'ResultDesc': 'The service request is processed successfully.', 'CallbackMetadata': {'Item': [{'Name': 'Amount', 'Value': 1.0}, {'Name': 'MpesaReceiptNumber', 'Value': 'NG421NVTR6'}, {'Name': 'Balance'}, {'Name': 'TransactionDate', 'Value': 20190704121251}, {'Name': 'PhoneNumber', 'Value': 254791836987}]}}}} 

# """




