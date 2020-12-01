import requests

res = requests.get('https://ipinfo.io/')
data = res.json()

city = data['city']

location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]
ip = data['ip']
timezone = data['timezone']
print(data, "\n")

print("Latitude : ", latitude)
print("Longitude : ", longitude)
print("City : ", city)
print("Ip address :", ip)
print("timezone: ", timezone)