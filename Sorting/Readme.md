#  Experimental Analysis on Sorting Algorithms

## Overview

For this analysis, I curated a diverse set of input data categorized into four distinct types. Each category encompasses datasets of varying sizes, specifically 20,000, 40,000, 80,000, 160,000, and 320,000 elements. The data categories are:

## Implemented Algorithms
* Insertion Sort
* Merge Sort
* Heapsort
* Quick Sort
* 3-way Merge Sort 

## Data Preparation

To conduct this analysis, I have prepared a diverse set of input data, classified into four categories, with each category containing datasets of varying sizes. The dataset sizes are 20,000, 40,000, 80,000, 160,000, and 320,000 elements. The data categories are:

**Random Data:** Unordered datasets of specified sizes.
**Sorted Random Data:** Random data sorted in ascending order.
**Reverse Sorted Random Data:** Random data sorted in descending order.
**Identical Data:** Datasets where all elements are the same.

In total, there are 20 unique datasets, with 5 sizes across the 4 data categories. These datasets are stored in separate files and are consistently used across all algorithms to ensure a fair comparison of performance.

## Analysis Focus

My analysis centers on three key aspects:

* Running time
* Number of comparisons
* Performance under different data conditions
  
The focus is on evaluating execution time and number of comparisons for each algorithm, providing insights into their efficiency and suitability for different data types.

**Data and Output**

Input: Diverse datasets of varying sizes.
Output: Detailed statistics including size of input, number of comparisons, and execution time.

## The key findings are:

**Insertion Sort:** Highly efficient for small or already sorted data sets, but less effective for larger, unsorted data.

**Merge Sort & 3-way Merge Sort:** Both perform well on larger data sets, with 3-way Merge Sort being theoretically more efficient but slower in practice due to increased comparisons.

**Heap Sort:** Ideal for large data sets and limited space, offering a balance between speed and space efficiency.

![image](https://github.com/gayathripittu/Data-Structures/assets/48981111/4c0cb0f0-d80b-44e1-be92-b22887873618)
![image](https://github.com/gayathripittu/Data-Structures/assets/48981111/064d9d32-fb1c-4db9-ae28-d678553166de)
![image](https://github.com/gayathripittu/Data-Structures/assets/48981111/11b7ce59-23da-43d1-87ba-9973a7a8d7e1)
![image](https://github.com/gayathripittu/Data-Structures/assets/48981111/66626b69-605f-4111-a634-1bf0c8cde854)





