# BFS Min-Hop Path Finder

## Overview

This Project aims to implement and analyze the Breadth-First Search (BFS) algorithm in a graph representing a network of airports and flight routes. The project's goal is to find the minimum-hop path between two nodes in the graph.

The challenge is to determine the shortest path, in terms of hops, between a given source and destination in a directed graph. This problem simulates finding the least number of flights needed to travel from one airport to another.

## Approach

The algorithm starts at the root node (source airport) and explores nodes level by level, ensuring no node is revisited. Nodes are colored to track their visitation status: White (unvisited), Gray (visited but not fully explored), and Black (fully explored).

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

The results of Project 2C demonstrate the BFS algorithm's effectiveness in solving the minimum-hop path problem in airport network graphs. Tests on graphs of varying sizes showed that the algorithm's performance aligns with its theoretical time complexity of O(V+E), where V is the number of vertices and E is the number of edges, confirming its efficiency and scalability for practical applications. 

This project highlights the BFS algorithm's utility in real-world graph problems.The experimental results confirmed the theoretical time complexity of O(V+E), where V is the number of vertices and E is the number of edges
