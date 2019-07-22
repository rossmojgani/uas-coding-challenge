#!/usr/bin/env python3

"""
Simple client script to connect to a server and accept
GPS coordinates in lattitude and longitude, convert
to UTM coordinates and calculate average speed in meters/second
"""

import socket, pickle, math
from pyproj import Proj
import numpy as np
from pandas import DataFrame

# pyproj object for zone 10U in northern hemisphere where missionwaypoints.txt coordinates are
myProj = Proj("+proj=utm +zone=10U, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")

# lists of lattitude and longitude
list_long_coords = []
list_lat_coords = []

if __name__ == '__main__':
    # create socket object and connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0', 8080))

    while True:
        try:
            # receive data from server and decode to string
            from_server = client.recv(4096)
            data = pickle.loads(from_server)
            
            # append longitude and lattitude to respective list
            list_long_coords.append(float(data[1]))
            list_lat_coords.append(float(data[0]))

            # convert longitude and lattiude to UTMx and UTMy lists
            df = DataFrame(np.c_[tuple(list_long_coords), tuple(list_lat_coords)], columns=['Longitude', 'Lattitude'])
            UTMx, UTMy = myProj(df['Longitude'].values, df['Lattitude'].values, inverse=False)
            
            # difference in x and y corrdinates in absolute value
            UTMx_diff = abs(UTMx[-1] - UTMx[0])
            UTMy_diff = abs(UTMy[-1] - UTMy[0])
            
            # using pythagorus thereom (a^2 + b^2 = c^2) to calculate difference in distance
            c_squared = UTMx_diff ** 2 + UTMy_diff ** 2
            c = math.sqrt(c_squared)
            meters_second = c / len(list_long_coords)
            
            print("Average speed in meters per second (m/s) is: {}".format(meters_second))
        except Exception as e:
            client.close()
            break

