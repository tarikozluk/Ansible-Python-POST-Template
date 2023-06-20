import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

def mail_app(url_adress,Dev_Team,service,istirak,http_https,SSL_izleme):

    url = "{}/api/v2/job_templates/142/launch/".format(os.getenv("AWX_ADRESS"))
    payload = {
        "extra_vars": {
            "url_adress": url_adress,
            "Dev_Team": Dev_Team,
            "service": service,
            "istirak": istirak,
            "http_https": http_https,
            "SSL_izleme": SSL_izleme
        }
    }

    headers = {
        'Authorization': 'Basic {}'.format(os.getenv("AWX_PASS")),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.text)
    print("Template is running")