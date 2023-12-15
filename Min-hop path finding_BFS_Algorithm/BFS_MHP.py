

import random
import time
import sys

def BFS_MHP(G, s):
    hopcount={}   # to store hopcount of each node
    parentlist={} # to store parent of each node
    color_of_node={} # to store color of each node
    for i in G:      # for every vertex in graph assiging colors, distance, hopcount intially
        if i==s:
            hopcount[i]=0
            parentlist[i]='NIL'
            color_of_node[i]='GRAY'
        else:
            hopcount[i]=float('inf')
            parentlist[i]='NIL'
            color_of_node[i]='WHITE'
    
    queue=[s]     # enqueue s
    
     # while will iterate until queue is empty
    while queue:
        u = queue.pop(0)  # poping the first element of list 
        for vertex in G[u]:   
            if color_of_node[vertex] == "WHITE":   # visiting node if the color is white
                color_of_node.update({vertex:'GRAY'}) # updating color of node to gray to avoid revisiting
                hopcount[vertex]=hopcount[u]+1         # next three lines: calculating hopcount and updating parent for each visited vertex and appending the vertex to queue
                parentlist[vertex]=u
                queue.append(vertex)         
        color_of_node.update({u:'BLACK'}) # updating color of node to black to avoid revisiting
    

    return parentlist           # returning the parent list for printing min hop path

def Print_SP(G,s,t,p,l):      #  min hop path function(graph,source,destination,parentlist,empty list to store path)
    if t==s:
        l.append(s)          
    elif p[t]=='NIL':          # we don't have parent for one vertex and we didn't reached destination, it means we don't have path so printing none
        return "None"
    else:
        Print_SP(G,s,p[t],p,l)      # will continue untill we reach destination
        l.append(t)
    return l

   
    
if __name__ == "__main__":
    v=int(sys.argv[1])             # number of vertices
    e=int(sys.argv[2])             # number of edges
    timelist=[]                    # a list is creating to store time of all 25 calls of program running time
    edges=[]                        # an empty edges list creation
    paths=[]                        # an empty paths list creation
    while(len(edges)<e):            # while loop will iterate untill we get 'e' number of edges into list
        x=random.randint(0,v-1)
        y=random.randint(0,v-1)
        if x!=y and [x,y] not in edges:
            edges.append([x,y])
    edges.sort(key = lambda edges:edges[0])
    # above created 'e' number of edges for 'v' nodes
    # now creating a dictionary to store adjacents of each node
    # In dictionary key is node and values is adjacents of node
    adjacencylist= [[] for i in range(v)]
    for i in edges:
        adjacencylist[i[0]].append(i[1])
    graph=dict()
    for i in range(v):
        graph[i]=adjacencylist[i]
    
    
    for i in range(25):            # iterating loop 25  function calls to calculate avg time 
        source=0
        dest=0
        while(source==dest):           # if we select randomly source and destination, we have a chance of getting same source and destination, am handling it here by comparing source and dest
            source=random.randint(0,v-1)
            dest=random.randint(0,v-1)               # will get random source and dest
        #print("Source and dest:",source,dest)
        #st=time.time()
        st=time.perf_counter_ns()         # time calculation
        parentlist=BFS_MHP(graph,source)
        #print(parentlist)
        l=[]
        l=Print_SP(graph,source,dest,parentlist,l)
        paths.append(l)
        et=time.perf_counter_ns()
        timelist.append(et-st) 
    k=random.randint(0,24)          # randomly generating one value to print any one of the path among 25
    r=paths[k]                     # appending the randomly choosen path to r
    if(r=="None"):
        print("None")
    else:
        for j in r:
            print(j,end=" ")
    print()
        
        #total_time=((time.time()-st)*(10**9))
           # stored every function call execution time
    print("Average of total time:",sum(timelist)/len(timelist))    # calculating avg of execution time 
        
        
        

  
  

   
