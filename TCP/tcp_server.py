import socket
import json

def main():
    # Define server address and port
    host = "127.0.0.1"  # The server will listen on this address
    port = 9000  # The port to listen for incoming connections

    try:
        # Create a TCP server socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Allow the port to be reused immediately after the server stops
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Bind the server socket to the host and port
            server_socket.bind((host, port))
            print(f"Server is listening on {host}:{port}")

            # Start listening for incoming connections (up to 5 simultaneous connections in the queue)
            server_socket.listen(5)

            while True:
                # Accept a new client connection
                client_socket, client_address = server_socket.accept()
                print(f"New connection from {client_address}")

                with client_socket:
                    while True:
                        try:
                            # Receive data from the client
                            data = client_socket.recv(1024)  # Buffer size of 1024 bytes
                            if not data:
                                # If no data is received, the client has disconnected
                                print(f"Connection closed by {client_address}")
                                break

                            # Decode the received data
                            json_data = data.decode('utf-8')
                            print(f"Received JSON string: {json_data}")

                            # Parse the JSON string into a Python dictionary
                            try:
                                parsed_data = json.loads(json_data)
                                print(f"Parsed Data: {parsed_data}")
                            except json.JSONDecodeError:
                                print("Received invalid JSON format.")

                        except ConnectionResetError:
                            print(f"Connection reset by {client_address}")
                            break

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
