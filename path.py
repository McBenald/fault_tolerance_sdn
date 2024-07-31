import requests

def discover_path(src_device_id, dst_device_id):
    # ONOS REST API URL for path discovery
    onos_ip = "127.0.0.1"  # Replace with your ONOS IP address
    onos_port = "8181"         # Replace with your ONOS port
    url = f"http://{onos_ip}:{onos_port}/onos/v1/paths?src={src_device_id}&dst={dst_device_id}"

    try:
        # Send a GET request to discover the path
        response = requests.get(url)

        if response.status_code == 200:
            path_info = response.json()
            return path_info
        else:
            print(f"Failed to discover path between {src_device_id} and {dst_device_id}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def main():
    src_device_id = 'of:0000000000000001'  # Replace with the source device ID
    dst_device_id = 'of:0000000000000002'  # Replace with the destination device ID

    path_info = discover_path(src_device_id, dst_device_id)
    if path_info:
        print("Path discovered:")
        for link in path_info['links']:
            print(f"Link: {link['src']} -> {link['dst']}")

if __name__ == '__main__':
    main()
    
