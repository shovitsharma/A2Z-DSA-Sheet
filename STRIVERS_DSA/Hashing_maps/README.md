# Hashing Maps Problems in Python

This folder contains Python implementations of hashing and frequency counting using Python dictionaries (hash maps). Each file demonstrates a different approach to solving frequency-related problems for both characters and integers. Below is a description of each file, the problem it solves, and a summary of the logic used.

---

## 1. `char_map_hash.py`
**Description:**
- Counts the frequency of each character in a list using a dictionary (hash map).

**Problem Solved:**
- Given a list of characters, efficiently count the frequency of each character and answer queries about the frequency of any character, even if the character set is not limited to ASCII.

**Logic Summary:**
- Uses a dictionary where the key is the ASCII value of the character. For each character, increments the count in the dictionary. Querying is done using the dictionary's `get` method for O(1) access.

---

## 2. `int_map_hash.py`
**Description:**
- Counts the frequency of each integer in a list using a dictionary (hash map).

**Problem Solved:**
- Given a list of integers (possibly with a large or unknown range), count the frequency of each integer and answer queries about the frequency of any integer.

**Logic Summary:**
- Uses a dictionary where the key is the integer value. For each integer, increments the count in the dictionary. Querying is done using the dictionary's `get` method for O(1) access.

---

## 3. `high_low_freqmap.py`
**Description:**
- Finds the highest and lowest frequency of elements in an integer array using a hash map.

**Problem Solved:**
- Given a list of integers, determine which frequency is the highest and which is the lowest among all unique elements.

**Logic Summary:**
- Builds a frequency dictionary for the array. Iterates through the values to find the maximum and minimum frequency without using built-in min/max functions.

---

Each file is self-contained and can be run directly. Input is taken from the user, and results are printed as output. Comments in each file explain the logic and steps in detail.
