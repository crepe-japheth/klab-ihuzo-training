from django.shortcuts import redirect
import requests
def make_payment(amount,name, email):

    print( amount)
    print( name)
    print( email)

    header = {'Authorization': 'Bearer ' + 'FLWSECK_TEST-653de16c61b6124ee6ba049f47215c4e-X'}
    data = {
        "tx_ref": "hooli-tx-1920bbtytty",
        "amount": amount,
        "currency": "RWF",
        "payment_options": "card",
        "redirect_url": "http://localhost:8000/",
        "meta": {
            "consumer_id": 23,
            "consumer_mac": "92a3-912ba-1192a"
        },
        "customer": {
            "email": email,
            "phonenumber": "0783378349",
            "name": name
        },
        "customizations": {
            "title": "Pied Piper Payments",
            "logo": "http://www.piedpiper.com/app/themes/joystick-v27/images/logo.png"
        }
    }
    url ="https://api.flutterwave.com/v3/payments"
    resp = requests.post(url, json=data, headers=header)
    resp = resp.json()
    print(resp)
    link = resp["data"]['link']
    
    
    return link