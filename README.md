# Understanding TCP, UDP, and Threading in Networking

This document provides a detailed overview of **TCP**, **UDP**, and **Threading** in networking, along with Python code examples for practical understanding.

---

## Table of Contents
- [What is TCP?](#what-is-tcp)
  - [Python TCP Server Example](#python-tcp-server-example)
  - [Python TCP Client Example](#python-tcp-client-example)
- [What is UDP?](#what-is-udp)
  - [Python UDP Server Example](#python-udp-server-example)
  - [Python UDP Client Example](#python-udp-client-example)
- [What is Threading?](#what-is-threading)
  - [Threaded TCP Server Example](#threaded-tcp-server-example)
  - [Threaded UDP Server Example](#threaded-udp-server-example)

---

## What is TCP?
**TCP (Transmission Control Protocol)** is a connection-oriented protocol that ensures reliable and ordered delivery of data between devices.

### Key Features:
- Reliable: Guarantees data delivery.
- Connection-oriented: Establishes a connection before data transfer.
- Data is delivered in sequence.

---

### Python TCP Server Example
This example creates a simple TCP server that listens for a connection, receives data, and prints it.

```python
import socket

def tcp_server():
    host = '127.0.0.1'  # Localhost
    port = 9000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)  # Listen for 1 connection
        print(f"Server is listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)  # Buffer size of 1024 bytes
                if not data:
                    break
                print(f"Received: {data.decode('utf-8')}")

if __name__ == "__main__":
    tcp_server()
```

---

### Python TCP Client Example
This example creates a TCP client that connects to the server and sends a message.

```python
import socket

def tcp_client():
    host = '127.0.0.1'
    port = 9000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = "Hello, Server!"
        client_socket.sendall(message.encode('utf-8'))
        print("Message sent!")

if __name__ == "__main__":
    tcp_client()
```

---

## What is UDP?
**UDP (User Datagram Protocol)** is a connectionless protocol used for faster, but less reliable, data transmission.

### Key Features:
- Connectionless: No setup required before sending data.
- Fast but unreliable: No guarantee of data delivery or order.

---

### Python UDP Server Example
This example creates a UDP server that listens for incoming data.

```python
import socket

def udp_server():
    host = '127.0.0.1'
    port = 9001

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"UDP Server is listening on {host}:{port}")

        while True:
            data, addr = server_socket.recvfrom(1024)  # Buffer size of 1024 bytes
            print(f"Received from {addr}: {data.decode('utf-8')}")

if __name__ == "__main__":
    udp_server()
```

---

### Python UDP Client Example
This example creates a UDP client that sends a message to the server.

```python
import socket

def udp_client():
    host = '127.0.0.1'
    port = 9001

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        message = "Hello, UDP Server!"
        client_socket.sendto(message.encode('utf-8'), (host, port))
        print("Message sent!")

if __name__ == "__main__":
    udp_client()
```

---

## What is Threading?
**Threading** allows you to run multiple tasks concurrently within the same program. In the context of networking, threading is used to handle multiple clients simultaneously.

### Key Features:
- Enables concurrency.
- Each thread runs independently.

---

### Threaded TCP Server Example
This example creates a TCP server that handles multiple clients using threads.

```python
import socket
import threading

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print(f"Connection closed by {client_address}")
                break
            print(f"Received from {client_address}: {data.decode('utf-8')}")

def threaded_tcp_server():
    host = '127.0.0.1'
    port = 9002

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)  # Allow up to 5 connections
        print(f"Threaded TCP Server is listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

if __name__ == "__main__":
    threaded_tcp_server()
```

---

### Threaded UDP Server Example
This example creates a UDP server that handles incoming messages concurrently using threads.

```python
import socket
import threading

def handle_message(data, addr):
    print(f"Received from {addr}: {data.decode('utf-8')}")

def threaded_udp_server():
    host = '127.0.0.1'
    port = 9003

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Threaded UDP Server is listening on {host}:{port}")

        while True:
            data, addr = server_socket.recvfrom(1024)
            client_thread = threading.Thread(target=handle_message, args=(data, addr))
            client_thread.start()

if __name__ == "__main__":
    threaded_udp_server()
```

---

## Conclusion
- Use **TCP** for reliable, connection-oriented communication.
- Use **UDP** for fast, connectionless communication.
- Use **Threading** to handle multiple clients or tasks concurrently.

Each protocol and technique has its use cases, and choosing the right one depends on your specific application requirements.

