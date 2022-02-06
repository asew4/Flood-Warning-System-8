# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine
from floodsystem.stationdata import build_station_list
from .station import MonitoringStation
from . import datafetcher

def stations_by_distance(stations, p):
    #Function to sort list of stations and their distance from a coordinate sorted by increasing distance
    stations = build_station_list()
    names = []
    distance = []
    for station in stations:
        names.append(station.name)
        distance.append(haversine(p, station.coord))
    overall_list = list(zip(names, distance))
    overall_list = sorted_by_key(overall_list,1)
    return overall_list

def stations_within_radius(stations, centre, r):
    #Function to name the stations that are within a radius, r, of a coordinate centre.
    stations = build_station_list()
    names =[]
    for station in stations:
        if haversine(centre, station.coord) <= r:
            names.append(station.name)
        else:
            pass
    return names

