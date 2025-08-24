import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
print(pepnumber)
location = phonenumbers.geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode


key="09d0d101b55a4e479cb470af91ca7c45"
geocoder = OpenCageGeocode(key)
qurey = str(location)
result =geocoder.geocode(qurey)

print(result)
lng=result[0]['geometry']['lng']
lat=result[0]['geometry']['lat']

myMap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")
