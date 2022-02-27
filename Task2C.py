#from floodsystem import geo
#from floodsystem.stationdata import build_station_list
from floodsystem.station import *
from floodsystem.flood import stations_highest_rel_level
####
from floodsystem.stationdata import *
from floodsystem.station import MonitoringStation

stations = build_station_list()
update_water_levels(stations)



print(stations_highest_rel_level(stations,10))