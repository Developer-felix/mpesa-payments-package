"""
Auther : Onjomba Felix
Phone : +254717713943
license : MIT
"""
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

class MpesaPayments:
    """
    The Definition of all the keys in the MpesaPayments class that are required
    """
    def __init__(self, businessshortCode,lipa_na_mpesa_pass_key,\
                      consumer_secret_key,consumer_key, call_back_url, account_reference, \
                       transaction_desc):
        self.businessshortCode = businessshortCode
        self.lipa_na_mpesa_pass_key =lipa_na_mpesa_pass_key
        self.consumer_secret_key = consumer_secret_key
        self.consumer_key = consumer_key
        self.call_back_url = call_back_url
        self.account_reference = account_reference
        self.transaction_desc = transaction_desc        
    
    def generate_timestamp(self):
        unformated_time = datetime.datetime.now()
        formated_time = unformated_time.strftime("%Y%m%d%H%M%S")
        return formated_time

    def generate_access_token(self):
        """
        getting the access tocken
        """
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        r = requests.get(api_URL, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret_key))
        json_response = r.json()
        my_access_token = json_response["access_token"]
        return my_access_token
    
    def generate_passoword(self):
        #creating password
        data_to_encode = self.businessshortCode + self.lipa_na_mpesa_pass_key + self.generate_timestamp()
        encoded_string = base64.b64encode(data_to_encode.encode())
        decoded_password = encoded_string.decode('utf8')
        return decoded_password
    
    """
    Lipa na mpesa online function to fire the stk push
    """
    def lipa_na_mpesa_online(self,phone_number,amount):
        access_tokens = self.generate_access_token()
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": f"Bearer {access_tokens}" ,"Content-Type": "application/json" }
        request = {
                    "BusinessShortCode": self.businessshortCode,
                    "Password": self.generate_passoword(),
                    "Timestamp": self.generate_timestamp(), # timestamp format: 20190317202903 yyyyMMhhmmss 
                    "TransactionType": "CustomerPayBillOnline",
                    "Amount": amount,
                    "PartyA": phone_number,
                    "PartyB": self.businessshortCode,
                    "PhoneNumber": phone_number,
                    "CallBackURL": self.call_back_url,
                    "AccountReference": self.account_reference,
                    "TransactionDesc": self.transaction_desc,
                }
        response = requests.post(api_url,json=request,headers=headers)
        print(response)

"""
Creating Object Mpesa That Carries all The Other Mpesa Details. 
Make sure you take these details from your .env files.
"""
# mpesa = MpesaPayments(
#     "174379",
#     "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1*******",
#     "qu7EEhC7SuLM6*****",
#     "CIeOGUScnbGinYoVawHAOPkRW7********************************",
#     "https://32fd-41-60-236-25.in.ngrok.io/payments/lnm/",
#     "Sky Plus Softwares",
#     "Sky Plus Softwares Description of C2B Payments"
# ) 

# """
# Call these function to make payments
# """
# print("Testing")
# print(mpesa.lipa_na_mpesa_online(
#     phone_number="254717713943",
#     amount=1
# ))

# # print(mpesa.generate_passoword())

