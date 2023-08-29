import requests
import time
import base64

host = "127.0.0.1"
port = "8181"
username = "onos"
password = "rocks"

credentials = base64.b64encode("{}:{}".format(username, password).encode("utf-8")).decode("utf-8")

def set_standby(switch_ID):
    url = "http://{}:8181/onos/v1/devices/of:0000000000000001/flows".format(host)

    headers = {
        "Content-type": "application/json",
        "Accept": "application/json",
        "Authorization":  "Basic {}".format(credentials)
    }

    data = {"role": "STANDBY"}

    

















