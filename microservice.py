# Example Client

import socket
import json
import os
from time import sleep
import readchar

# 'method': 'filter', 'start': '2024-02-01', 'end': '2025-03-22'
data = [
    {'method': 'filter', 'start': '2024-02-01', 'end': '2025-03-22'},
    {'id': 0, 'date': '2025-06-23'}, {'id': 1, 'date': '2024-01-01'},
    {'id': 2, 'date': '2024-12-23'}, {'id': 3, 'date': '2024-06-11'},
    {'id': 4, 'date': '2025-04-23'}, {'id': 5, 'date': '2024-04-07'},
    {'id': 6, 'date': '2024-12-11'}, {'id': 7, 'date': '2024-05-11'},
    {'id': 8, 'date': '2024-06-23'}, {'id': 9, 'date': '2024-04-21'},
    ]



def send_request(data):
    # Get the hostname and initiate the port
    host = socket.gethostname()
    port = 5000

    # Get instance and connect to the server
    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
    except ConnectionRefusedError:
        print("The connection to the server was refused")
        return
    # Convert data to JSON and send it
    print("Sending data to server")
    data_send = json.dumps(data).encode('utf-8')
    client_socket.sendall(data_send)
    
    # Receive the data back
    data_recv = client_socket.recv(8192)
    print("Receiving data from server")
    new_data = json.loads(data_recv.decode('utf-8'))
    print("Data Received")
    for item in new_data:
        print(item)
    sleep(5)

    # Close the connection
    client_socket.close()


while True:
    os.system('cls')
    print("Main Menu")
    print("\n\n1. Send Socket Request")
    print("2. Quit\n\n")

    print("Enter a selection")
    keystroke = readchar.readkey()
    match keystroke:
        case '1':
            send_request(data)
        case '2':
            os._exit(0)
        case _:
            pass
