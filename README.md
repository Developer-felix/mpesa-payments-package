
## Mpesa Payments (C2B, B2C) Package
<img src="pypi.png" alt="PyPi Image" /> 

- I have repeatedly created the same code while creating lipa na mpesa online payments systems. This is the write time to stop the code repeating on every projects that involves payments. I decided not to become selfish and also come up with these package for the new developers and also the python developers in the industries.

- mpesa_paymens is a python package thet contains B2C and C2B payments methods. It creates stk push and allows you to serve it with all the details of mpesa payments.


###  Install

- step 1 : Create Account On Daraja and have these details Bellow 
      
- step 2 : Pip Install The Library as bellow:

        $ pip install mpesa-payments 


### Usage

Creating Object Mpesa That Carries all The Other Mpesa Details. 
Make sure you take these details from your .env files.


```
from mpesa_paymens.mpesa_paymens import MpesaPayments

mpesa = MpesaPayments(
     "businessshortCode",
     "lipa_na_mpesa_pass_key",
     "consumer_secret_key",
     "consumer_key", 
     "call_back_url", 
     "account_reference", 
     "transaction_desc"
) 
``` 

Call these function to make payments 

```
mpesa.lipa_na_mpesa_online(
    phone_number="254717713943",
    amount=1
))
```

## Example

```
from mpesa_paymens.mpesa_paymens import MpesaPayments

mpesa = MpesaPayments(
     "174379",
     "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1*******",
     "qu7EEhC7SuLM6*****",
     "CIeOGUScnbGinYoVawHAOPkRW7********************************",
     "https://32fd-41-60-236-25.in.ngrok.io/payments/lnm/",
     "Sky Plus Softwares",
     "Sky Plus Softwares Description of C2B Payments"
) 


mpesa.lipa_na_mpesa_online(
    phone_number="25471771****",
    amount=1
)
```

## Asumptions
I assume that you understand the the call back url concepts.

### License

This project is licensed under the MIT License


### Author

[Onjomba Felix Abere ](http://github.com/developer-felix)

## Hire Me 
Email : onjombafelix1@gmail.com
Phone : +254717713943
