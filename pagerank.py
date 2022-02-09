# python pagerank.py
from py2neo import Graph
from py2neo import Node, Relationship
import pandas as pd
import numpy as np

my_graph = Graph(password='root')

my_graph.run("CALL gds.graph.create('myGraph1','street','to' )")
pageRank = my_graph.run("CALL gds.pageRank.stream('myGraph1') YIELD nodeId, score RETURN gds.util.asNode(nodeId).edge AS IdStreet, score ORDER BY score DESC, IdStreet ASC")
print(pageRank)
lst=pageRank.data()
print(type(pageRank.data()))
print(lst)
df=pd.DataFrame(columns=['IdStreet', 'score'])
for val in lst :
    df = df.append(val, ignore_index=True)

print(df)

index=df[df['IdStreet']=='403397173#2'].index
df.drop(index,inplace=True)

df2=df[df['score']<0.6]

llst=[]
for index, row in df2.iterrows():
    var1=my_graph.run("match (c:street{edge:'"+row['IdStreet']+"'}) <-[r:to]-(m) return r")
    for k in var1.data():
        if k['r']['vehid'] not in llst :
            llst.append(k['r']['vehid'])

print(llst)

