# Change Making Problem Analysis with Dynamic Programming

## Overview

The "Change Making Problem Analysis with Dynamic Programming" project explores the classic problem in computer science, focusing on finding the minimum number of coins needed to make change for a given amount using a set of coin denominations. It involves the implementation and analysis of solutions specifically using Dynamic Programming. The primary goal is to examine the efficiency and performance of the Dynamic Programming approach in solving this practical problem, which finds applications in scenarios such as vending machines or financial software.

## Problem Description

Given an amount n (in cents) that needs to be changed and a coin system consisting of k denominations, denoted as d1, d2, ..., dk, the primary goal is to find the minimum number of coins required to make the change. Each denomination di has an associated value in cents.

**Example**

Consider a scenario where the amount to be changed is 63 cents (n = 63), and the coin system is based on the US currency, including denominations of penny (1 cent), nickel (5 cents), dime (10 cents), and quarter (25 cents). The coin system is represented as [1, 5, 10, 25].

The goal is to find a combination of coins that minimizes the total count while summing up to the given amount. In the provided example, a potential optimal solution could be:

* 2 quarters (25 cents each)
* 1 dime (10 cents)
* 3 pennies (1 cent each)

This combination adds up to 63 cents (2 * 25 + 1 * 10 + 3 * 1) and requires the minimum number of coins (6 coins in this case).

## Data Preparation

The project uses various test cases with different coin systems, including:

* Standard U.S. coin system (penny, nickel, dime, quarter)
* Custom coin systems with unique denominations

## Implemented Algorithm

**Dynamic Programming Solution:** Utilizes a bottom-up dynamic programming approach to find the minimum number of coins needed for making change. Expected time complexity: O(k.n)

## Test the Algorithm solution on the following inputs:

* Test on the US coin system with k = 4 and denominations [1, 5, 10, 25].

* Test on a custom coin system with 5 denominations (penny, nickel, dime, 23 cents, quarter) with k = 5 and denominations [1, 5, 10, 23, 25]

## Output Format

The output should include a list of integers representing the coins used and the time required to compute the solution.

## Key Findings

**Dynamic Programming:** Showed optimal performance in terms of both time complexity and accuracy.
**Greedy Algorithm:** While faster in some cases, it does not always guarantee the optimal solution.
**Recursive Approach:** Less efficient due to its exponential time complexity, useful for understanding the problem's nature.

