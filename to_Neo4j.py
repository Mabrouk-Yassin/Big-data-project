# python to_Neo4j.py
from kafka import KafkaConsumer
from json import loads
import os
import sys
import optparse
import json
import xmltodict
from time import sleep
from kafka import KafkaProducer
from py2neo import Graph
from py2neo import Node, Relationship
import sys

# In[16]:


from kafka import KafkaProducer

# mytopic
consumer = KafkaConsumer("mytopic3",
                     bootstrap_servers=['localhost:9092'],
                     group_id=None,
                     auto_offset_reset='earliest')

my_graph = Graph(password='root')

for message in consumer:
    message = message.value
    jsonCnv= json.loads(message)
    my_graph.run("MERGE (labels:vehicle {vehid:'"+jsonCnv['vehid']+"'})")
    if jsonCnv['edge'] == '403397173#2' :
        my_graph.run("MERGE (labels:street {edge:'"+jsonCnv['edge']+"'})")
        my_graph.run("MATCH(a:vehicle {vehid:'"+jsonCnv['vehid']+"'}) MATCH(m:street {edge:'"+jsonCnv['edge']+"'}) MERGE(a)-[:here]->(m)")

        continue
    else:
        my_graph.run("MERGE (labels:street {edge:'"+jsonCnv['edge']+"'})")
        tnp = my_graph.run("match (a:vehicle {vehid:'"+jsonCnv['vehid']+"'}) - [r:here] -> (c) return (c) ")


        var = tnp.data()[0]["c"]["edge"]
        if var != jsonCnv['edge']:
            my_graph.run("MATCH(a:street {edge:'"+var+"'}) MATCH(m:street {edge:'"+jsonCnv['edge']+"'}) MERGE(a)-[:to {vehid:'"+jsonCnv['vehid']+"'}]->(m)")
            my_graph.run("MATCH(a:vehicle {vehid:'"+jsonCnv['vehid']+"'}) - [r:here] -> () delete r ")
            my_graph.run("MATCH(a:vehicle {vehid:'"+jsonCnv['vehid']+"'}) MATCH(m:street {edge:'"+jsonCnv['edge']+"'}) MERGE(a)-[:here]->(m)")




sys.exit()

