import numpy as np
import matplotlib


def polyfit(dates, levels, p):
    
    x = matplotlib.dates.date2num(dates)    #Returns list of floats rather than list of datetime
    y = levels

    p_coeff = np.polyfit(x - x[0], y, p) #Using shifted values of x, finds coefficients of best-fit polynomial f(x) of degree p

    poly = np.poly1d(p_coeff) #Converts coefficient into polynomial that can be evaluated

    return poly, x[0]