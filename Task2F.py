import py_compile
from floodsystem import plot
from floodsystem import datafetcher
from floodsystem import stationdata
from floodsystem import utils
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def highest_stations(n, stations):
    stationdata.update_water_levels(stations)
    highest_levels = []
    for station in stations:
        if station.latest_level == None:
            pass
        elif station.latest_level >= 90:
            pass
        else:
            highest_levels.append((station, station.latest_level))
        sorted_highest_levels = utils.sorted_by_key(highest_levels, 1)
    return sorted_highest_levels[-n:]
    


def run():
    stations = stationdata.build_station_list()
    five_stations = highest_stations(5, stations)
    dt = 2
    for i in five_stations:
        dates, levels = datafetcher.fetch_measure_levels(i[0].measure_id, dt=timedelta(days=dt))
        plot.plot_water_level_with_fit(i[0], dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
    
