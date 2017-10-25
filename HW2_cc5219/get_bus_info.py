from __future__ import print_function
import requests
import json
import os
import sys
import numpy as np
import pandas as pd
key=sys.argv[1]
busline=sys.argv[2]
filename=sys.argv[3]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + busline
requrl = requests.get(url)
data=requrl.json()
buses= data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
numbus=np.size(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
bus_info = pd.DataFrame(columns=['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])
for i in range(numbus):
    lat = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    lon = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    businfo=buses[i]['MonitoredVehicleJourney']['OnwardCalls']
    onwardcall= businfo.get('OnwardCall','Not Found')
    if onwardcall=='Not Found':
        stopname='N/A'
        busstauts='N/A'
    else:
        stopname=businfo['OnwardCall'][0].get('StopPointName','N/A')
        busstatus=businfo['OnwardCall'][0]['Extensions']['Distances'].get('PresentableDistance','N/A')
    df = pd.DataFrame({'Latitude': [lat], 'Longitude': [lon], 'Stop Name': stopname, 'Stop Status': busstatus})
    bus_info = bus_info.append(df)
    df = df.reset_index(drop=True)
    bus_info.to_csv(filename)

