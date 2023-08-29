data={'Body': 
{'stkCallback':
 {'MerchantRequestID': '23481-4888433-1', 'CheckoutRequestID': 'ws_CO_DMZ_384585971_04072019121246169', 'ResultCode': 0, 'ResultDesc': 'The service request is processed successfully.', 
 'CallbackMetadata': 
 {'Item': 
 [{'Name': 'Amount', 'Value': 1.0}, 
 {'Name': 'MpesaReceiptNumber', 'Value': 'NG421NVTR6'}, 
 {'Name': 'Balance'}, 
 {'Name': 'TransactionDate', 'Value': 20190704121251}, 
 {'Name': 'PhoneNumber', 'Value': 254791836987}
 ]}
 }
 }
} 
from datetime import datetime
# data=request.data

testcode=(data['Body']['stkCallback']['ResultCode'])
MerchantRequestID=(data['Body']['stkCallback']['MerchantRequestID'])
CheckoutRequestID=(data['Body']['stkCallback']['CheckoutRequestID'])
ResultCode = (data['Body']['stkCallback']['ResultCode'])
ResultDescription = (data['Body']['stkCallback']['ResultDesc'])
Amount=(data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value'])
mpesa_receipt_number=(data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value'])
MpesaReceiptNumber=''
TransactionDate=(data['Body']['stkCallback']['CallbackMetadata']['Item'][3]['Value'])
# convert date
TransactionDate=str(TransactionDate)
TransactionDate=datetime.strptime(TransactionDate,("%Y%m%d%H%M%S"))

PhoneNumber=(data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value'])

# print(TransactionDate)

mpesa_data_callbk={
    "testcode":testcode,
    "MerchantRequestID":MerchantRequestID,
    "CheckoutRequestID":CheckoutRequestID,
    "ResultCode":ResultCode,
    "Amount":Amount,
    "mpesa_receipt_number":mpesa_receipt_number,
    "TransactionData":TransactionDate,
    "PhoneNumber":PhoneNumber
}

print(TransactionDate)