# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town




    ##Task1F
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
                             typical_range=(5., 1.),
                             river='riv6',
                             town='town6') 
station7 = MonitoringStation(station_id='stat6',
                             measure_id='test_measure_id_1',
                             label='Station 6',
                             coord=(4., 5.),
                             typical_range= None,
                             river='riv6',
                             town='town6')
from floodsystem.station import *

def test_typical_range_consistant():
    #stations = [station1, station2, station3, station4, station5, station6, station7]
    assert station7.typical_range_consistant() == False
    assert station6.typical_range_consistant() == False



def test_inconsistant_typical_range_stations():
    stat_data = [station4, station5, station6, station7]
    assert inconsistant_typical_range_stations([station4]) == []
    assert inconsistant_typical_range_stations([station6]) == [station6.name]





