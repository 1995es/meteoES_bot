import requests

url_g = "https://maps.googleapis.com/maps/api/geocode/json"

key_g = "AIzaSyBIg5XoO3KTKWJEQO7u-oAGxG6C-OV7TfA"

payload_g = {
    "address" : "Totana, Espana",
    "key" : key_g,
    "language" : "es"
}

r_g = requests.get(url=url_g, params=payload_g)

response = r_g.json()
print r_g.url
#print r_g.text

lat = response["results"][0]["geometry"]["location"]["lat"]
lng = response["results"][0]["geometry"]["location"]["lng"]

print lat
print lng

url = "https://api.darksky.net/forecast/"

key = "fa340435f77d438c330c299f60bcaf5f/"

key_google = "AIzaSyBWuh2HN2WLugFD1rGZFMmwkzy7JCdlCgQ"

#latlng = "37.8267,-122.4233"
latlng = str(lat) + str(",") + str(lng) 

params = {
    "lang" : "es",
    "units" : "si",
    "exclude" : "minutely, hourly, daily"
}

url = url + key + latlng
r = requests.get(url=url, params=params)

print r.url
print r.text

