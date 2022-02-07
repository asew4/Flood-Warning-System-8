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
#    assert isinstance(station_distance[0],MonitoringStation)




##Task 1D Tests
from floodsystem.geo import *
def test_rivers_with_stations():
    stations = build_station_list()
    function_test = rivers_with_stations(stations)
    assert "River Thames" in function_test


def test_stations_by_river():
    stations = build_station_list()
    function_test = stations_by_river(stations)
    assert "River Tees" in function_test



##Task 1E Tests
#sample_data = [ ('River Great Ouse', 30), ('River Derwent', 25), ('River Thames', 55), ('River Avon', 31), ('River Aire', 24), ('River Calder', 23), ('River Severn', 21), ('River Stour', 21), ('River Ouse', 18), ('River Colne', 18)]

#def test_rivers_by_station_number():
#    stations = build_station_list()
#    function_test = rivers_by_station_number(stations,1)
#    assert ('River Thames',55) in function_test









