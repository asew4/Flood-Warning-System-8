
#Test for stations_by_distance function (Task 1B)
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def test_stationsbydistance():
    stations = build_station_list()
    station_distance = stations_by_distance(stations, (52,0.1))
    assert sorted_by_key(station_distance, 1) == station_distance
    assert isinstance(station_distance[0][1],float)

#Test for stations_within_radius function (Task 1C)
from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation

def test_stationswithinradius():
    stations = build_station_list()
    station_distance = stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert isinstance(station_distance[0],MonitoringStation)
