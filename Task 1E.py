from floodsystem import geo
from floodsystem.stationdata import build_station_list


stations = build_station_list()

print(geo.rivers_by_station_number(stations,9))