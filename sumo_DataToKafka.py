############## sumo_DataToKafka.py
import traci
import time
import traci.constants as tc
import pytz
import datetime
from random import randrange
import pandas as pd
from time import sleep
from kafka import KafkaConsumer, KafkaProducer
from json import loads
import os
import sys
import optparse
import json
import xmltodict
import xml.etree.ElementTree as ET
from kafka import KafkaProducer


sumoCmd = ["sumo", "-c", "berrechid.sumo.cfg"]
traci.start(sumoCmd)

packVehicleData = []
packTLSData = []
packBigData = []

while traci.simulation.getMinExpectedNumber() > 0:
       
        traci.simulationStep();

        vehicles=traci.vehicle.getIDList();
        trafficlights=traci.trafficlight.getIDList();

        for i in range(0,len(vehicles)):


                vehid = vehicles[i]
                x, y = traci.vehicle.getPosition(vehicles[i])
                coord = [x, y]
                lon, lat = traci.simulation.convertGeo(x, y)
                gpscoord = [lon, lat]
                spd = round(traci.vehicle.getSpeed(vehicles[i])*3.6,2)
                edge = traci.vehicle.getRoadID(vehicles[i])
                lane = traci.vehicle.getLaneID(vehicles[i])
                displacement = round(traci.vehicle.getDistance(vehicles[i]),2)
                turnAngle = round(traci.vehicle.getAngle(vehicles[i]),2)
                nextTLS = traci.vehicle.getNextTLS(vehicles[i])

                #Packing of all the data for export to CSV/XLSX
                vehList = [vehid, coord, gpscoord, spd, edge, lane, displacement, turnAngle, nextTLS]

                

                print(vehicles[i], " >>> Position: ", coord, " | GPS Position: ", gpscoord, " |", \
                                       " Speed: ", round(traci.vehicle.getSpeed(vehicles[i])*3.6,2), "km/h |", \
                                      #Returns the id of the edge the named vehicle was at within the last step.
                                       " EdgeID of veh: ", traci.vehicle.getRoadID(vehicles[i]), " |", \
                                      #Returns the id of the lane the named vehicle was at within the last step.
                                       " LaneID of veh: ", traci.vehicle.getLaneID(vehicles[i]), " |", \
                                      #Returns the distance to the starting point like an odometer.
                                       " Distance: ", round(traci.vehicle.getDistance(vehicles[i]),2), "m |", \
                                      #Returns the angle in degrees of the named vehicle within the last step.
                                       " Vehicle orientation: ", round(traci.vehicle.getAngle(vehicles[i]),2), "deg |", \
                                      #Return list of upcoming traffic lights [(tlsID, tlsIndex, distance, state), ...]
                                       " Upcoming traffic lights: ", traci.vehicle.getNextTLS(vehicles[i]), \
                       )

                idd = traci.vehicle.getLaneID(vehicles[i])

                tlsList = []

                packBigDataLine = vehList

                packBigData.append(packBigDataLine)

                ##------------------------------------------------------##


traci.close()

columnnames = ['vehid', 'coord', 'gpscoord', 'spd', 'edge', 'lane', 'displacement', 'turnAngle', 'nextTLS']


dataset = pd.DataFrame(packBigData, index=None, columns=columnnames)
time.sleep(5)
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
for index, row in dataset.iterrows():
    dct={}

    for column in columnnames :
        dct[column]=str(row[column])

    producer.send('mytopic3', dct)


