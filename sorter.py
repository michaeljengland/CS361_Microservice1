# Server

import json
import socket
from time import sleep

# Takes a list of dictionaries and sorts by date in ascending order
# Returns a sorted list without modifying the existing list
def sort_ascending(story_list):
    # Remove the dictionary containing the method
    new_list = story_list[1:]
    
    # Sort the list
    sorted_list = sorted(new_list, key=lambda x: x['date'])
    
    return sorted_list

# Takes a list of dictionaries and sorts by date in descending order
# Returns a sorted list without modifying the existing list
def sort_descending(story_list):
    # Remove the dictionary containing the method
    new_list = story_list[1:]
    
    # Sort the list
    sorted_list = sorted(new_list, key=lambda x: x['date'])
    sorted_list.reverse()
    
    return sorted_list

# Takes a list of dictionaries and filters them by date
# Returns a filtered list without modifying the existing list
def date_filter(story_list):
    # Initialize variables
    start_date = story_list[0]['start']
    end_date = story_list[0]['end']
    new_list = []

    # Filter the list
    for item in story_list[1:]:
        if item['date'] >= start_date and item['date'] <= end_date:
            new_list.append(item)

    return new_list


# Main program loop
while True:
    # Get the hostname and initiate the port
    host = socket.gethostname()
    port = 5000

    # Get instance and bind host address and port
    server_socket = socket.socket()
    server_socket.bind((host, port))

    # Configure how many clients the server can listen to simultaneously
    server_socket.listen(1)

    # Accept a new connection
    conn, address = server_socket.accept()


    while True:
        # Receive data stream and set max number of bytes to receive
        data = conn.recv(8192)

        # If no data is received, break
        if not data:
            break

        # Receive data and convert it from JSON 
        print("Received from connected user")
        data_recv = json.loads(data.decode('utf-8'))
        sleep(2)
        print("Processing data")

        # Check for the requested process
        if data_recv[0]['method'] == 'asc':
            new_data = sort_ascending(data_recv)
        elif data_recv[0]['method'] == 'desc':
            new_data = sort_descending(data_recv)
        else:
            new_data = date_filter(data_recv)
        sleep(2)

        # Convert to JSON and send the data back
        print("Sending data back to client")
        data_send = json.dumps(new_data).encode('utf-8')
        conn.sendall(data_send)

    # Close the connection
    conn.close()
