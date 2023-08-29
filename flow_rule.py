import requests
import json
import base64

host = "127.0.0.1"
port = "8181"
username = "onos"
password = "rocks"

credentials = base64.b64encode("{}:{}".format(username, password).encode("utf-8")).decode("utf-8")

def install_flow_rule(device_ID):
    url = "http://{}:8181/onos/v1/devices/of:0000000000000001/flows".format(host)
    #url = "http://{}:{}/onos/v1/flows".format(host, port)
    headers = {
        "Content-type": "application/json",
        "Accept": "application/json",
        "Authorization":  "Basic {}".format(credentials)
    }

    data = {
        "priority": 50000,
        "timeout": 0,
        "isPermanent": True,
        "deviceID": "of:0000000000000001",
        "treatment": {
            "instructions":[
                {
                    "type": "OUTPUT",
                    "port": 2
                }
            ]
        },
        "selector": {
            "criteria":[
                {
                    "type": "ETH_TYPE",
                    "ethType": "0x0800"
                },
                {
                    "type": "IPV4_DST",
                    "ip": "200.0.0.0/24"
                }
            ]
        }
    }

    response = requests.post(url, headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Flow rule installed successfully!")
    else:
        print("Failed to install flow rule. Error {}".format(response.text))