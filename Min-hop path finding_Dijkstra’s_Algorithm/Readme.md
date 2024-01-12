# Dijkstra's Algorithm for Shortest Path

## Overview

This Project aims to implement Dijkstra's algorithm to find the shortest path in a graph representing a network of airports and flight routes. The focus is on computing the shortest path based on flight lengths (weights) between two airports.

The challenge is to determine the shortest path in terms of distance (flight length) between a given source and destination in a directed graph. This simulates finding the shortest flight route in terms of miles between two airports.

## Approach

The project uses Dijkstra's algorithm, which systematically explores nodes, always selecting the node with the shortest known distance from the start.

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

The results of Project 2C demonstrate the BFS algorithm's effectiveness in solving the minimum-hop path problem in airport network graphs. Tests on graphs of varying sizes showed that the algorithm's performance aligns with its theoretical time complexity of O(V+E), where V is the number of vertices and E is the number of edges, confirming its efficiency and scalability for practical applications. 

This project highlights the BFS algorithm's utility in real-world graph problems.The experimental results confirmed the theoretical time complexity of O(V+E), where V is the number of vertices and E is the number of edges
