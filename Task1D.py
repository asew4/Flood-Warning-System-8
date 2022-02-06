from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
stat = build_station_list()
#from floodsystem import geo






print(len(rivers_with_stations(stat)), "Rivers with one or more stations")
print((sorted(rivers_with_stations(stat))[:10]))
print('')

print("River Aire has stations: ", sorted((stations_by_river(stat))['River Aire']))
print('')
print("River Thames has stations: ", sorted((stations_by_river(stat))['River Thames']))
#print(sorted(rivers_with_stations(stat)))
#print(rivers_with_stations(stat))
#print(rivers_morethanone_station(stat))
