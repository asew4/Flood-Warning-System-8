from . import datafetcher
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
import numpy as np
from floodsystem.analysis import polyfit
import matplotlib

def plot_water_levels(station, dates, levels):

    # Plot
    typical_range = station.typical_range

    low_range = typical_range[0]
    high_range = typical_range[1]

    plt.plot(dates, levels)
    plt.axhline(y= low_range, color= 'r', linestyle = '-')
    plt.axhline(y= high_range, color= 'g', linestyle = '-')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    x1 = np.linspace(x[0], x[-1], 50)
    # Plot
    typical_range = station.typical_range

    low_range = typical_range[0]
    high_range = typical_range[1]

    plt.plot(dates, levels)

    poly_line = polyfit(dates, levels, p)
    y = poly_line[0]
    plt.plot(x1, y(x1 - x[0]))
    
    plt.axhline(y= low_range, color= 'r', linestyle = '-')
    plt.axhline(y= high_range, color= 'g', linestyle = '-')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()