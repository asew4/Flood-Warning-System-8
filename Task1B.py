from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list() #Sort through all stations on database
    p = (52.2053,0.1218) #Centre of Cambridge coordinate so can find distance of stations from here

    list = stations_by_distance(stations, p) #Creating list of stations and their distance from centre of Cambridge
    print("CLOSEST:", list[:10]) #Printing ten closest stations and their distances
    print("FURTHEST:", list[-10:]) #Printing ten furthest stations and their distances

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()