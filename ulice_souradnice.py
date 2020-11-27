import geopy.geocoders
from geopy.geocoders import Nominatim
geopy.geocoders.options.default_user_agent = 'Edg/86.0.622.43'
geolocator = Nominatim()
location = geolocator.geocode("49.171838,16.558271", language = "cz")
nazev = location.raw['display_name']
ulice = nazev.split(",")
if len(ulice) == 9:
    print(ulice[1])
elif len(ulice) == 8:
    print(ulice[0])
else:
    print(ulice)