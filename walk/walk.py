from collections import Mapping
# input = "mississippi"
input = "AAABBBBA"
import numpy as np
from collections import *
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()

def get_n_mers(input=input, n=3):
    arr = []
    for x in range(len(input)-(n-1)):
        arr.append(input[x:x+n])
    return arr

def get_n_minus_1_mers(input=input):
    arr = []
    for x in input:
        arr.append(x[0:len(x)-1])
        arr.append(x[1:len(x)])
    return arr

x = get_n_mers(input, 3)
print(x)
print("expected number of vertices =", len(x))
y = get_n_minus_1_mers(x)
print(y)
z=set(y)
print("expected number of edges =", len(z))
print("these are the nodes =", z)

input = ['AA', 'AA', 'AA', 'AB', 'AB', 'BB', 'BB', 'BB', 'BB', 'BB', 'BB', 'BA']
#input = ['mi', 'is', 'is', 'ss', 'ss', 'si', 'si', 'is', 'is','ss', 'ss', 'si', 'si', 'ip', 'ip', 'pp', 'pp', 'pi']

def build_graph(input=input):
    graph = {}
    arrlen = len(input)
    for i in range(0,len(input)-1,2):
        pair_a = input[i]
        pair_b = input[i+1]
        #print(pair_a, pair_b)
        if pair_a == pair_b:
            if pair_a not in graph:
                graph[pair_a] = []
                #G.add_node(pair_a)
            graph[pair_a].append(pair_b)
            #G.add_edge(pair_a, pair_b)
            #print(G.graph)
        elif pair_a != pair_b:
            if pair_a not in graph:
                graph[pair_a] = []
                #G.add_node(pair_a)
            if pair_b not in graph[pair_a]:
                graph[pair_a].append(pair_b)
                #G.add_edge(pair_a, pair_b)
            if pair_b not in graph:
                graph[pair_b] = []
                #G.add_node(pair_b)
    return graph


output = build_graph(y)
print(output)
g = nx.Graph(output)
#print(g.nodes)
#print(g.edges)
#nx.draw(G)
#plt.show()

nx.draw(G,with_labels=True)
plt.draw()
plt.show()

