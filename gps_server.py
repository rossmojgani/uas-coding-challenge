#!/usr/bin/env python3

"""
Server code to publish GPS coordinates once per second
from a text file
"""

import socket, pickle
from time import sleep

COORDINATES_FILE = "missionwaypoints.txt"

if __name__ == '__main__':
    # create socket object
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind to port 8080
    serv.bind(('0.0.0.0', 8080))
    serv.listen(5)

    while True:
        # accept client connection
        conn, addr = serv.accept()
        coordinates_file = open(COORDINATES_FILE, 'r')

        while True:
            line = coordinates_file.readline()
            # if line is invalid close connection
            if not line:
                break

            line = line.replace('\n', '')
            tup_lat_long = (line.split(",")[0], line.split(",")[1])
            # use pickles import to encode data for sending bytes over socket
            data = pickle.dumps(tup_lat_long)
            conn.send(data)
            # publish once a second so sleep for 1 second
            sleep(1)

        conn.close()
        print("Client disconnected")


