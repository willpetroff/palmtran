import requests

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
          'Referrer': 'http://www.palmtran.org/igo'}
# http://www.palmtran.org/iGo/rest/Vehicles/GetAllVehicles
target = 'http://www.palmtran.org/iGo/rest/Vehicles/GetAllVehiclesForRoutes?routeIDs=1'

request = requests.get(target, headers=HEADER)
data = [item for item in  request.json()]
for item in data:
    print(item)