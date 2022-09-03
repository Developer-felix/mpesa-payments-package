from mpesa_payments.mpesa_payments import MpesaPayments

mpesa = MpesaPayments(
    "174379",
    "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
    "qu7EEhC7SuLM6IIY",
    "CIeOGUScnbGinYoVawHAOPkRW7rNFbM0",
    "https://32fd-41-60-236-25.in.ngrok.io/payments/lnm/",
    "Sky Plus Softwares",
    "Sky Plus Softwares Description of C2B Payments"
)

"""
Call these function to make payments
"""

print(mpesa.lipa_na_mpesa_online(
    phone_number="25471771****",
    amount=1
))
print(mpesa.generate_passoword())