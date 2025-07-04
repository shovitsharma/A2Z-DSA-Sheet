# Sorting Algorithms in Python

This folder contains Python implementations of classic sorting algorithms. Each file demonstrates a different sorting technique, with clear comments and explanations. Below is an overview of each algorithm and its code structure.

## 1. Bubble Sort (`bubble_sort.py`)
- **Description:**
  - Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
  - The process is repeated until the list is sorted.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Key Points:**
  - Simple, but inefficient for large datasets.
  - In-place sorting (no extra space needed).

## 2. Insertion Sort (`insertion_sort.py`)
- **Description:**
  - Builds the sorted array one element at a time by repeatedly picking the next element and inserting it into its correct position among the already sorted elements.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Key Points:**
  - Efficient for small or nearly sorted datasets.
  - In-place sorting.

## 3. Selection Sort (`selection_sort.py`)
- **Description:**
  - Divides the array into a sorted and unsorted part, repeatedly selects the minimum element from the unsorted part, and moves it to the end of the sorted part.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Key Points:**
  - Simple, but not stable.
  - In-place sorting.

## 4. Merge Sort (`merge_sort.py`)
- **Description:**
  - A divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and then merges the sorted halves.
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Key Points:**
  - Stable and efficient for large datasets.
  - Not in-place (requires extra space for merging).

## 5. Recursive Bubble Sort (`recursive_bubble.py`)
- **Description:**
  - A recursive version of bubble sort, where the largest element is moved to the end in each recursive call.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Key Points:**
  - Demonstrates recursion with sorting.

## 6. Recursive Insertion Sort (`recursive_insertion.py`)
- **Description:**
  - A recursive version of insertion sort, where the array is sorted up to the (n-1)th element, and the nth element is inserted in the correct position.
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Key Points:**
  - Demonstrates recursion with sorting.
## 7. Quick Sort (`quick_sort.py`)
- **Description:**
  -A recursive implementation of the Quick Sort algorithm that follows the divide-and-conquer strategy.
- **Time Complexity:** O(nlogn)
- **Space Complexity:** O(1)
- **Key Points:**
  - Demonstrates recursion and partitioning.

---

Each file is self-contained and can be run directly. Input is taken from the user, and the sorted array is printed as output. Comments in each file explain the logic and steps in detail.

Feel free to explore each file for more details and experiment with different inputs!
