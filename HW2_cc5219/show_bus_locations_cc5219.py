
from __future__ import print_function
import requests
import json
import urllib.request as ulr
import os
import sys
key=sys.argv[1]
busline=sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef="+ busline
requrl = requests.get(url)
data=requrl.json()
buses= data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
activebus=0
print ("Bus Line: %s"%(busline))
for i in range(len(buses)):
     if buses[i]['MonitoredVehicleJourney']['PublishedLineName'] == busline:
        activebus += 1
        lattd = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lontd = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print("Bus %s is at latitude %s and longtitude %s" %(activebus,lattd,lontd))
