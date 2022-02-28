from floodsystem import stationdata
import pytest
import numpy as np
from floodsystem import datafetcher
from datetime import timedelta
from floodsystem import analysis
import matplotlib

stations = stationdata.build_station_list()

stationdata.update_water_levels(stations)

def test_analysis():
    dt = 5
    dates, levels = datafetcher.fetch_measure_levels(stations[0].measure_id, dt=timedelta(days=dt))
    x = matplotlib.dates.date2num(dates)

    poly, date_0 = analysis.polyfit(dates, levels, 3 )
    assert date_0 == x[0]
    assert isinstance(poly, np.poly1d)