# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from sqlalchemy import LargeBinary
from .utils import sorted_by_key  # noqa


#Task 1D
def rivers_with_stations(stations):
    rivers_with_stations = []
    for station in stations:
        if station.river != None:
            rivers_with_stations += [station.river]
            #print(station.name)
        
    return set(rivers_with_stations)


def check_for_duplicates(list):
    #simple check for duplicates
    if len(list) == len(set(list)):
        return False
    else:
        return True

def stations_by_river(stations):
    dict_rivers = {}
    for station in stations:
        dict_rivers[station.river] = None


    for river in dict_rivers:
        river_stations = []
        for station in stations:
            if station.river == river:
                river_stations += [station.name]

        dict_rivers[river] = river_stations


    return dict_rivers



#Task 1E
def rivers_by_station_number(stations, N):
    
    ##generate a list of rivers
    rivers = []
    for station in stations:
        rivers =  rivers + [station.river]
    rivers = set(rivers)

    ##generate a list of station numbers for each river
    rivers_with_stations = []
    for river in rivers:
        station_num = 0
        for station in stations:
            if station.river == river:
                station_num += 1
        rivers_with_stations.append((river,station_num))

    #return rivers_with_stations
    sorted_rivers_with_stations = sorted(rivers_with_stations, reverse = True, key=lambda i:i[1])
    #return sorted_rivers_with_stations
    
    large = sorted_rivers_with_stations[:N]

    for river in sorted_rivers_with_stations:
        nth_river = large[N-1]
        if river[1] == nth_river[1]:
            large += [river]

    print(len(large))
    return large


    



        
