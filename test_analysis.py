from os import times
from floodsystem import stationdata
import pytest
import numpy as np
from floodsystem import datafetcher
from datetime import timedelta
from floodsystem import analysis
from matplotlib import dates

stations = stationdata.build_station_list()

stationdata.update_water_levels(stations)

def test_analysis():
    dt = 10
    times, levels = datafetcher.fetch_measure_levels(stations[0].measure_id, dt=timedelta(days=dt))
    x= dates.date2num(times)

    poly, date_0 = analysis.polyfit(times, levels, 2)
    assert date_0 == x[0]

