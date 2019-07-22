# uas-coding-challenge
Coding challenge for UBC Unmanned Aircraft Systems

#### GPS Speed Challenge
You are tasked with making an application that computes the speed of an object (aircraft) given a series of GPS coordinates. Your application should be made of two programs: One program serves the GPS coordinates, and the other receives the coordinates and calculates the speed. You can use whatever method you would like for the serving (REST, serial, TCP serial, websockets, etc.). Use C++ or Python 3. 

Rules:
- GPS coordinates are provided here.
- Speed should be in either knots or meters per second.
- The speed should be the average speed over the whole series.
- The GPS coordinates are 1 second apart.

Bonuses:
- Return the current speed of the aircraft, updating once a second.


