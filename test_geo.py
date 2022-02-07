#Test for stations_by_distance function (Task 1B)
from cProfile import label
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from haversine import haversine

def test_stationsbydistance():
    #Create sample stations
    
    station_1 = MonitoringStation(label= 'Test Station 1', station_id= 'Test Station ID 1', measure_id= 'Test measure ID 1', coord= (0.0, 1.0), typical_range= (0.0,1.0), river= 'Test River 1', town= 'Test town 1')
    station_2 = MonitoringStation(label= 'Test Station 2', station_id= 'Test Station ID 2', measure_id= 'Test measure ID 2', coord= (1.0, 1.0), typical_range= (1.0,1.0), river= 'Test River 2', town= 'Test town 2')
    #Make a list of stations and sort
    
    stations = [station_1, station_2]
    sorted_stations = stations_by_distance(stations, (1.0, 1.0))
    assert sorted_stations[0] == ('Test Station 2', haversine((1.0,1.0),(1.0,1.0)))
    assert sorted_stations[1] == ('Test Station 1', haversine((1.0,1.0),(0.0,1.0)))
    



#Test for stations_within_radius function (Task 1C)
from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation

def test_stationswithinradius():
    stations = build_station_list()
    station_distance = stations_within_radius(stations, (52.2053, 0.1218), 10)
#    assert isinstance(station_distance[0],MonitoringStation)

station1 = MonitoringStation(station_id='stat1',
                             river='riv1',
                             measure_id='test_measure_id_1',
                             label='Station 1',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             town='town1')
station2 = MonitoringStation(station_id='stat2',
                             measure_id='test_measure_id_1',
                             label='Station 2',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             river='riv2',
                             town='town2')
station3 = MonitoringStation(station_id='stat3',
                             measure_id='test_measure_id_1',
                             label='Station 3',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             river='riv3',
                             town='town3')
station4 = MonitoringStation(station_id='stat4',
                             river='riv1',
                             measure_id='test_measure_id_1',
                             label='Station 4',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             town='town4')
station5 = MonitoringStation(station_id='stat5',
                             measure_id='test_measure_id_1',
                             label='Station 5',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             river='riv5',
                             town='town5')
station6 = MonitoringStation(station_id='stat6',
                             measure_id='test_measure_id_1',
                             label='Station 6',
                             coord=(4., 5.),
                             typical_range=(0., 1.),
                             river='riv6',
                             town='town6')                               

##Task 1D Tests
from floodsystem.geo import *

def test_river_by_station_number():
    station1 = MonitoringStation(station_id='stat1',
                                 river='riv1',
                                 measure_id='test_measure_id_1',
                                 label=' Station 1',
                                 coord=(4., 5.),
                                 typical_range=(0., 1.),
                                 town='town1')
    station2 = MonitoringStation(station_id='stat2',
                                 measure_id='test_measure_id_1',
                                 label=' Station 1',
                                 coord=(4., 5.),
                                 typical_range=(0., 1.),
                                 river='riv1',
                                 town='town2')
    station3 = MonitoringStation(station_id='stat3',
                                 measure_id='test_measure_id_1',
                                 label=' Station 1',
                                 coord=(4., 5.),
                                 typical_range=(0., 1.),
                                 river='riv3',
                                 town='town3')
    stations = [station1, station2, station3]
    function_test = rivers_by_station_number(stations,1)
    assert ('riv1',2) in function_test

def test_rivers_with_stations():
    stations = [station1, station2, station3]
    function_test = rivers_with_stations(stations)
    assert "riv1" in function_test
    assert len(function_test) == 3


def test_stations_by_river():

    stations = [station1, station2, station3, station4, station5, station6]
    function_test = stations_by_river(stations)
    assert 'Station 1' in ((stations_by_river(stations))['riv1'])
    assert 'Station 4' in ((stations_by_river(stations))['riv1'])



##Task 1E Tests
#sample_data = [ ('River Great Ouse', 30), ('River Derwent', 25), ('River Thames', 55), ('River Avon', 31), ('River Aire', 24), ('River Calder', 23), ('River Severn', 21), ('River Stour', 21), ('River Ouse', 18), ('River Colne', 18)]

#def test_rivers_by_station_number():
#    stations = build_station_list()
#    function_test = rivers_by_station_number(stations,1)
#    assert ('River Thames',55) in function_test









