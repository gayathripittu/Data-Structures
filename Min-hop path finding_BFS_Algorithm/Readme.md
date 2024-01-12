# BFS Min-Hop Path Finder

## Overview

This Project aims to implement and analyze the Breadth-First Search (BFS) algorithm in a graph representing a network of airports and flight routes. The project's goal is to find the minimum-hop path between two nodes in the graph.

The challenge is to determine the shortest path, in terms of hops, between a given source and destination in a directed graph. This problem simulates finding the least number of flights needed to travel from one airport to another.

## Approach

**Graph Representation:** The directed graph, representing airports and flight routes, is implemented using adjacency lists. This data structure efficiently handles sparse graphs as is often the case with airport networks.

**BFS Algorithm Customization:** The standard BFS algorithm is adapted to prioritize the minimum number of hops (edges) between nodes. This involves tracking the level of each node in the BFS tree to determine the shortest path in hops.

**Node Visitation Logic:** Nodes are marked with different statuses (unvisited, visited but not explored, and fully explored) to prevent revisiting and ensure efficient path finding.

**Path Reconstruction:** After reaching the destination node, the path is reconstructed from the BFS tree, ensuring the route with the minimum hops is identified.

**Execution Time Measurement:** The algorithm's performance is measured by calculating the execution time for each run, allowing for analysis against different graph sizes.

**Testing with Varying Graph Sizes:** The implementation is tested on four differently sized graphs to evaluate scalability and performance consistency.

## Input and Output

#### Input: 

A directed graph with specified nodes (airports) and edges (flight routes), and designated source and destination airports.
#### Output: 

The shortest path (minimum-hop) between the source and destination, and the execution time of the algorithm.

## Graph Sizes and Experimental Analysis

Four graphs of increasing sizes were tested:

- 25 nodes and 50 edges
- 50 nodes and 200 edges
- 100 nodes and 800 edges
- 200 nodes and 3200 edges
  
The graphs were randomly generated. The algorithm's performance was evaluated based on average execution times over multiple runs with different source and destination combinations.

## Results

The results of the project demonstrate the effectiveness of the BFS algorithm in solving the minimum-hop path problem in airport network graphs. Tests on graphs of varying sizes showed that the algorithm's performance aligns with its theoretical time complexity of O(V+E), where V is the number of vertices and E is the number of edges. This confirms its efficiency and scalability for practical applications.

