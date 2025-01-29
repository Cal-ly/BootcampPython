import json
import socket
import requests  # REMINDER: Install the requests library with "pip install requests" if not already installed.

# UDP Configuration
UDP_IP = "127.0.0.1"  # The IP address the proxy listens on (localhost in this case).
UDP_PORT = 44555  # The port the proxy listens on for incoming UDP messages.

# REST API Endpoint
API_URL = "https://chairapi-a2ggarbthrb4h4dr.northeurope-01.azurewebsites.net/api/chair/"

# Proxy Server Function
def main():
    """
    Starts a UDP proxy server that listens for UDP messages, parses them as JSON,
    and forwards valid JSON objects to a specified REST API endpoint.
    """
    print(f"Starting UDP proxy on {UDP_IP}:{UDP_PORT}, forwarding to {API_URL}")
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the specified IP and port
    sock.bind((UDP_IP, UDP_PORT))

    try:
        # Continuous loop to receive and process messages
        while True:
            # Receive a UDP message
            # recvfrom returns the data and the address of the sender
            data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
            print(f"Received message from {addr}: {data}")

            try:
                # Decode the received data from bytes to a UTF-8 string
                # Attempt to parse the decoded string as JSON
                chair = json.loads(data.decode('utf-8'))
                print(f"Parsed Chair: {chair}")

                # Forward the parsed JSON to the REST API using an HTTP POST request
                response = requests.post(API_URL, json=chair)
                
                # Check the response status code and print appropriate messages
                if response.status_code == 201:  # 201 indicates successful creation
                    print("Successfully forwarded to API.")
                else:
                    print(f"Failed to forward to API. Status: {response.status_code}, Response: {response.text}")

            except json.JSONDecodeError as e:
                # Handle JSON parsing errors
                print(f"JSON decode error: {e}")
            except requests.RequestException as e:
                # Handle HTTP request errors
                print(f"Error forwarding data to API: {e}")

    except Exception as e:
        # Handle any unexpected errors in the main loop
        print(f"An error occurred: {e}")
    finally:
        # Ensure the socket is closed when the program exits
        sock.close()

if __name__ == "__main__":
    main()