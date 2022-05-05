from geopy.geocoders import Nominatim
import geopy.distance

def find_distance(coords_1, coords_2):
    return geopy.distance.geodesic(coords_1, coords_2).miles

def get_coords(location):
    return (location.latitude, location.longitude)

geolocator = Nominatim(user_agent="Project 4")
location = geolocator.geocode("34 Cross street Malden MA" )
location2 = geolocator.geocode("4 Doane road medford MA" )
print((location.latitude, location.longitude))


print('The distance between the two locations is', find_distance(get_coords(location), get_coords(location2)), 'miles')


