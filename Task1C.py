from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list() #Sort through all stations on database
    centre = (52.2053, 0.1218) #Making centre of Cambridge the place to measure distances from
    r = 10 #Maximum radius (in km) from Cambridge for stations

    list = stations_within_radius(stations, centre, r) #Creating list of stations within 10km radius of Cambridge centre
    print(sorted(list)) #Printing list of these stations in alphabetical order

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()