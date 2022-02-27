from floodsystem.station import MonitoringStation
from floodsystem.stationdata import *


##Task 2B
def stations_level_over_threshold(stations, tol):
    station_list = []
    
    for station in stations:
        if station.relative_water_level() is not None and station.relative_water_level() > tol:
            station_list += [(station.name, station.relative_water_level())]
        else:
            pass


    return sorted(station_list, key = lambda b: b[1], reverse=True)
