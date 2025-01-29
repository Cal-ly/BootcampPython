
import json
import random
import socket
import time

# UDP Configuration
UDP_IP = "127.0.0.1"  # The IP address to which the broadcaster will send messages (localhost in this case).
UDP_PORT = 44555  # The port number for the UDP communication.

# Chair Data Template
def create_chair():
    """
    Creates a new chair object with random attributes.
    The chair object includes:
      - Model: A hardcoded value "RandomChair".
      - MaxWeight: A random integer between 50 and 200.
      - HasPillow: A random boolean value (True or False).
    Returns:
        dict: A dictionary representing the chair object.
    """
    return {
        "Model": "RandomChair",
        "MaxWeight": random.randint(50, 200),  # Random weight between 50 and 200.
        "HasPillow": random.choice([True, False])  # Randomly assign True or False.
    }

# UDP Broadcaster
def main():
    """
    Starts a UDP broadcaster that sends a JSON-encoded chair object to a specific IP and port every 5 seconds.
    """
    print(f"Starting UDP broadcaster on {UDP_IP}:{UDP_PORT}")
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            # Create a new chair object
            chair = create_chair()
            
            # Convert the chair object to a JSON string and encode it to bytes
            message = json.dumps(chair).encode('utf-8')
            
            # Send the encoded message to the specified IP and port
            sock.sendto(message, (UDP_IP, UDP_PORT))
            print(f"Sent: {message}")
            
            # Wait for 5 seconds before sending the next message
            time.sleep(5)

    except KeyboardInterrupt:
        # Gracefully handle script termination (e.g., via Ctrl+C)
        print("\nBroadcaster stopped.")
    finally:
        # Ensure the socket is properly closed
        sock.close()

if __name__ == "__main__":
    main()
