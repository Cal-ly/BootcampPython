import socket
import json

def main():
    # Define server address and port
    server_address = "127.0.0.1"  # Replace with your server's IP if needed
    port = 9000  # Replace with the port your SocketTest server is listening on

    try:
        # Create a TCP client socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_address, port))
            print("Connected to the server!")

            while True:
                # Get input from the user
                name = input("Enter your Name: ")
                race = input("Enter your Race: ")
                age = input("Enter your Age: ")

                # Validate and prepare data
                try:
                    age = int(age)  # Ensure age is an integer
                except ValueError:
                    print("Invalid age. Please enter a numeric value.")
                    continue

                # Create a dictionary for the data
                data = {"Name": name, "Race": race, "Age": age}

                # Serialize the dictionary to a JSON string
                json_data = json.dumps(data)

                # Send the JSON string to the server
                client_socket.sendall(json_data.encode('utf-8'))
                print(f"Data sent to server: {json_data}")

                # No response expected; just loop again
                print("\nReady to send another input...\n")

    except ConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
