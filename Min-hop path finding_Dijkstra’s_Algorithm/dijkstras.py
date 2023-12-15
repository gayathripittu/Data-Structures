import random 
import time
import heapq
import sys


# graph generate function
def generate_graph(v,e):
    nodes = [i for i in range(v)]
    edges = []
    while len(edges)<e:      #loop will iterate untill we get specified number of edges
        x = random.randint(0,v-1)    # randomly creating edges
        y = random.randint(0,v-1)
        if x!=y and [x,y] not in edges:
            edges.append([x, random.randint(300,2000), y])   #assigning randomly weight to edges between 300 and 2000

    
    adj_list = [[] for i in range(v)]     # creating adjacency list
    for i in edges:
        adj_list[i[0]].append((i[1],i[2])) # appending weight and adjacency nodes to each vertex
    adj_list_dic = []
    graph = {i:adj_list[i] for i in range(v)}   # creating graph from adjacency list
    return graph       

def dijk(graph,source,dest):
    queue = [(0, source, ())]            # adding source weight and source and path to queue
    S = set()                            # creating set
    distance={source: 0.0}               # intializing source distance
    while queue:                         # while loop will iterate until queue is empty
        weight, v, path = heapq.heappop(queue)     # poping the minimum from queue
        if v not in S:                  # adding vertex into set if it is not present in set already
            S.add(v)
            path += (v,)                # adding vertex to shortest path
            if v == dest:               # if we reached the destination returning the path and weight
                return (weight, path)
            
            for weight2, v2 in graph.get(v, ()):       
                if v2 in S:
                    continue
                if weight + weight2 < distance.get(v2, float('inf')): # relaxination 
                    distance[v2] = weight + weight2
                    heapq.heappush(queue, (weight + weight2, v2, path))  # updating distance
    return float('inf'), ()                  


if __name__=='__main__':
    v=int(sys.argv[1])             # number of vertices
    e=int(sys.argv[2])             # number of edges
    graph = generate_graph(v,e)
    #print(graph)
    timelist=[]
    l=[]
    source=0
    dest=0
    while(source==dest):           # if we select randomly source and destination, we have a chance of getting same source and destination, am handling it here by comparing source and dest
        source=random.randint(0,v-1)
        dest=random.randint(0,v-1) # will get random source and dest


    for i in range(25):            # iterating loop 25  function calls to calculate avg time 
        source=0
        dest=0
        while(source==dest):           # if we select randomly source and destination, we have a chance of getting same source and destination, am handling it here by comparing source and dest
            source=random.randint(0,v-1)
            dest=random.randint(0,v-1)               # will get random source and dest
        st=time.perf_counter_ns()         # time calculation
        weight, short_path=dijk(graph,source,dest)
        et=time.perf_counter_ns()
        timelist.append(et-st)    # appending each call time to calculate avg time
 


    
    if(short_path):
        print(short_path)     # if we have path between source and destination printing ShortestPath, else printing none
    else:
        print("None")
    print("Average of total time:",sum(timelist)/len(timelist))    # calculating avg of execution time 
