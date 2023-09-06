import requests

def set_switch_to_standby(switch_dpid):
    # ONOS REST API URL to set the switch to standby
    onos_ip = "127.0.0.1"  # Replace with your ONOS IP address
    onos_port = "8181"         # Replace with your ONOS port
    url = "http://{}:{}/onos/v1/devices/{}/role/STANDBY".format(onos_ip, onos_port, switch_dpid)

    # Send a PUT request to set the switch to standby
    response = requests.put(url)

    if response.status_code == 200:
        print(f"Switch {switch_dpid} set as standby successfully.")
    else:
        print(f"Failed to set switch {switch_dpid} as standby.")

def main():
    switch_dpid = '0000000000000010'  # DPID of the switch you want to set as standby
    set_switch_to_standby(switch_dpid)

if __name__ == '__main__':
    main()