import requests
import json

def register_external_service(consul_url, name, address, port):
    port = int(port) #Convert to int since we get a string from AWS API
    headers = {'Content-type': 'application/json'}
    data = {'Node': name, 'Address': address, 'Service': {'Service': name, 'Port': port}}
    r = requests.put(consul_url + '/v1/catalog/register', data=json.dumps(data), headers=headers)
