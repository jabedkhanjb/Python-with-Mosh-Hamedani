import phonenumbers
import opencage
import folium

number = input("Enter a number: ")

from phonenumbers import geocoder
tracing_number = phonenumbers.parse(number)
print(f"here is your number: {number} \n{tracing_number}")

location = geocoder.description_for_number(tracing_number, "en")
print(f"Your number is located in {location}")

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key = "4c82d068d9e94767ab16b1ec1b9d67b5" #website: opencagedata.com

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = result[0]["geometry"]["lat"]
lng = result[0]["geometry"]["lng"]
print(lat, lng)

googlemap = folium.Map(location = [lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location).add_to(googlemap)

googlemap.save("number track file.html")
