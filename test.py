#!/usr/bin/env python

import ecef_to_geodetic

import numpy as np

def ecef_to_geodetic_python(x, y, z):
    a = 6378137.0  # Semi-major axis (meters)
    f = 1 / 298.257223563  # Flattening
    e2 = 2 * f - f * f  # Eccentricity squared

    lon = np.arctan2(y, x)
    p = np.sqrt(x**2 + y**2)
    lat = np.arctan2(z, p * (1 - e2))

    for _ in range(7):  # Increased iterations for better precision
        N = a / np.sqrt(1 - e2 * np.sin(lat)**2)
        alt = p / np.cos(lat) - N
        lat = np.arctan2(z, p * (1 - e2 * (N / (N + alt))))

    return np.degrees(lat), np.degrees(lon), alt

if __name__ == "__main__":
    x, y, z = 1113194.907, 1113194.907, 6356752.314

    start_time = time.time()
    lat, lon, alt = ecef_to_geodetic_python(x, y, z)
    runtime = time.time() - start_time
    print("--- Python ------------------------------")
    print(f"X,Y,Z: {x},{y},{z}")
    print(f"Latitude: {lat}°")
    print(f"Longitude: {lon}°")
    print(f"Altitude: {alt} meters")
    print(f"Runtime: {runtime} second(s)")

    print("--- Native ------------------------------")
    start_time = time.time()
    lat, lon, alt = ecef_to_geodetic.convert(x, y, z)
    runtime = time.time() - start_time
    print(f"X,Y,Z: {x},{y},{z}")
    print(f"Latitude: {lat}°")
    print(f"Longitude: {lon}°")
    print(f"Altitude: {alt} meters")
    print(f"Runtime: {runtime} second(s)")


    # expected results
    #Latitude: 76.17710632709549°
    #Longitude: 45.0°
    #Altitude: 190811.72193944734 meter(s)

