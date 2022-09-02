from django.shortcuts import render

from mpesa_payments.mpesa_payments import MpesaPayments

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

mpesa = MpesaPayments(
    "174379",
    "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
    "qu7EEhC7SuLM6IIY",
    "CIeOGUScnbGinYoVawHAOPkRW7rNFbM0",
    "https://32fd-41-60-236-25.in.ngrok.io/payments/lnm/",
    "Sky Plus Softwares",
    "Sky Plus Softwares Description of C2B Payments"
) 

@csrf_exempt
@api_view(["GET","POST"])
def payments(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        amount = request.POST.get("amount")

        try:
            mpesa.lipa_na_mpesa_online(
                phone=phone, 
                amount= amount
                )
            return Response({"success": False, "status_code": 1,"message": "OK"})
        
        except:
            return Response({"success": True, "status_code": 1,"message": "Failure"})


