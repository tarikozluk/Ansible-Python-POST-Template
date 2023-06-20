import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()


def mail_redis(server_1, server_2, server_3, server_4, service, istirak):

    url = "{}/api/v2/job_templates/{}/launch/".format(os.getenv("AWX_ADRESS"),os.getenv("AWX_TEMPLATE_ID"))

    payload = {
        "extra_vars": {
            "server_1": server_1,
            "server_2": server_2,
            "server_3": server_3,
            "server_4": server_4,
            "service": service,
            "istirak": istirak
        }
    }
    print(payload)

    headers = {
        'Authorization': 'Basic {}'.format(os.getenv("AWX_PASS")),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.text)
    print("Template is running")

