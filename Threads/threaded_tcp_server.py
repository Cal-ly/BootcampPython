import socket
import json
import threading

# Function to handle each client in a separate thread
def handle_client(client_socket, client_address):
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
                print(f"Received JSON string from {client_address}: {json_data}")

                # Parse the JSON string into a Python dictionary
                try:
                    parsed_data = json.loads(json_data)
                    print(f"Parsed Data: {parsed_data}")
                except json.JSONDecodeError:
                    print(f"Invalid JSON format from {client_address}")

            except ConnectionResetError:
                print(f"Connection reset by {client_address}")
                break
            except Exception as e:
                print(f"Error handling client {client_address}: {e}")
                break

    print(f"Client {client_address} disconnected.")

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

                # Create a new thread to handle the client
                client_thread = threading.Thread(
                    target=handle_client, args=(client_socket, client_address)
                )
                client_thread.start()
                print(f"Started thread for {client_address}")

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
