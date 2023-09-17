import requests

def set_switch_to_standby(switch_dpid):
    # ONOS REST API URL to set the switch to standby
    onos_ip = "127.0.0.1"  # Replace with your ONOS IP address
    onos_port = "8181"         # Replace with your ONOS port
    url = "http://{}:{}/onos/v1/devices/{}/role/STANDBY".format(onos_ip, onos_port, switch_dpid)

    # Send a PUT request to set the switch to standby
    response = requests.put(url)

    if response.status_code == 200:
        print("Failed to set switch {} as standby.".format(switch_dpid))

    else:
        print("Switch {} set as standby successfully.".format(switch_dpid))

def main():
    switch_dpid = '0000000000000010'  # DPID of the switch you want to set as standby
    set_switch_to_standby(switch_dpid)

if __name__ == '__main__':
    main()