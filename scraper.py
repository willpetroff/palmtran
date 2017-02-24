from requests import get
import csv
from time import sleep
from datetime import datetime

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
          'Referrer': 'http://www.palmtran.org/igo'}

target = 'http://www.palmtran.org/iGo/rest/Vehicles/GetAllVehicles'



request = get(target, headers=HEADER)
while request.status_code == 200:
    with open('palmtran.csv', 'a', newline='') as csv_file:
        data = [ [
                     item['TripId'],
                     item['RouteId'],
                     item['RunId'],
                     item['VehicleId'],
                     item['Latitude'],
                     item['Longitude'],
                     item['Speed'],
                     item['Deviation'],
                     item['LastStop'],
                     item['Direction'],
                     item['DirectionLong'],
                     item['OnBoard'],
                     item['Destination'],
                     item['Name'],
                     item['LastUpdated'],
                     item['Heading'],
                     item['OpStatus'],
                     item['DisplayStatus'],
                     item['GPSStatus'],
                     item['CommStatus'],
                     item['BlockFareboxId'],
                     item['DriverName'],
                 ] for item in request.json()]
        writer = csv.writer(csv_file)
        writer.writerows(data)
    sleep(45)
    request = get(target, headers=HEADER)
print(str(datetime.now()), request.status_code)
