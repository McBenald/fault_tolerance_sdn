import json
import requests

# Set up the API URL and authentication
url = "http://127.0.0.1:8181/onos/v1/acl/rules"
username = "onos"
password = "rocks"

# Read the firewall rules from a JSON file
policy_file = "rules.json"
with open(policy_file, 'r') as jsonfile:
    firewall_rules = json.load(jsonfile)

# Remove firewall rules (optional)
response = requests.delete(url, auth=(username, password))
print(response.status_code)

# Create firewall rules using the ONOS API
for rule in firewall_rules:
    response = requests.post(url, json=rule, auth=(username, password))
    print(response.text)

if response.status_code == 201:
    print("firewall rule set successfully.")
else:
    print("firewall rule not set successfully.")
    
