# Dijkstra's Algorithm for Shortest Path

## Overview

This Project aims to implement Dijkstra's algorithm to find the shortest path in a graph representing a network of airports and flight routes. The focus is on computing the shortest path based on flight lengths (weights) between two airports.

The challenge is to determine the shortest path in terms of distance (flight length) between a given source and destination in a directed graph. This simulates finding the shortest flight route in terms of miles between two airports.

## Approach

**Graph Initialization:** The graph, representing an airport network, is initialized with nodes (airports) and weighted edges (flight routes). An adjacency list or matrix is used for efficient data representation.

**Set Up Data Structures:** A priority queue is set up to manage nodes during the algorithm's execution. Additional structures store the shortest distance to each node from the source and track the nodes' visitation status.

**Implementing Dijkstra's Algorithm:**

* Initialize all node distances as infinite, except for the source node, set to zero.
* Insert the source node into the priority queue.
* While the priority queue is not empty, repeat the following:
     * Remove the node with the smallest distance from the priority queue.
     * For each unvisited neighbor of this node, calculate the distance from the source. If 
       this distance is less than the currently known distance, update it.
     * Mark the node as visited.

**Path Reconstruction:** After reaching the destination or exhausting all nodes, the shortest path is reconstructed from the source to the destination using the stored data.

**Performance Analysis:** Execution time is measured and analyzed, providing insights into the algorithm's efficiency across various graph sizes.

## Input and Output

#### Input: 

A directed graph with nodes (airports), edges (flight routes), and weights (flight lengths in miles).

#### Output: 

The shortest path in terms of distance between the source and destination airports, along with the algorithm's execution time.

## Graph Sizes and Experimental Analysis

Four graphs of increasing sizes were tested:

- G1: 25 nodes, 50 edges
- G2: 50 nodes, 200 edges
- G3: 100 nodes, 800 edges
- G4: 200 nodes, 3200 edges
  
Edges were assigned random weights between 300 to 2000 miles. The algorithm's performance was evaluated for execution time and correctness.

## Results

Dijkstra's algorithm was successfully applied to determine the shortest paths in graph-based airport networks. The results, consistent across different graph sizes, affirm the algorithm's efficiency and reliability. This underscores the practical relevance of Dijkstra's algorithm in solving real-world network routing problems, demonstrating its applicability and robustness in complex scenarios like optimizing flight routes.
