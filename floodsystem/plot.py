from . import datafetcher
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
import numpy as np
from floodsystem.analysis import polyfit
import matplotlib

def plot_water_levels(station, dates, levels):

    #Defining values for upper and lower range for graph
    typical_range = station.typical_range
    low_range = typical_range[0]
    high_range = typical_range[1]

    #Plotting the current level, average lower range level horizontal line and average upper range level horizontal line
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

    #Defining values for upper and lower range for graph
    typical_range = station.typical_range
    low_range = typical_range[0]
    high_range = typical_range[1]

    #Plotting the current levels
    plt.plot(dates, levels)

    #Using Polyfit function to create line of best fit of current levels
    poly_line = polyfit(dates, levels, p)
    y = poly_line[0]
    plt.plot(x1, y(x1 - x[0]))
    
    #Plotting the average lower range level horizontal line and average upper range level horizontal line
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