# Hashing Problems in Python

This folder contains Python implementations of basic hashing techniques for both characters and integers. Each file demonstrates a different approach to hashing and frequency counting. Below is a description of each file, the problem it solves, and a summary of the logic used.

---

## 1. `char_hashing.py`
**Description:**
- Demonstrates character frequency counting using a fixed-size array (hash array) for ASCII characters.

**Problem Solved:**
- Given a list of characters, efficiently count the frequency of each character and answer queries about the frequency of any character.

**Logic Summary:**
- Uses an array of size 256 (for all ASCII characters). For each character, increments the count at the index corresponding to its ASCII value. Querying is done in O(1) time by accessing the array at the ASCII index of the character.

---

## 2. `int_hashing.py`
**Description:**
- Demonstrates integer frequency counting using a fixed-size array (hash array) for a known range of integers.

**Problem Solved:**
- Given a list of integers within a known range, count the frequency of each integer and answer queries about the frequency of any integer.

**Logic Summary:**
- Uses an array where the index represents the integer value. For each integer, increments the count at the corresponding index. Querying is done in O(1) time by accessing the array at the integer's index. Handles out-of-range queries gracefully.

---

## 3. `char_map_hash.py`
**Description:**
- Demonstrates character frequency counting using a dictionary (hash map) for characters.

**Problem Solved:**
- Given a list of characters, count the frequency of each character and answer queries, even if the character set is not limited to ASCII.

**Logic Summary:**
- Uses a dictionary where the key is the ASCII value of the character. For each character, increments the count in the dictionary. Querying is done using the dictionary's `get` method for O(1) access.

---

## 4. `int_map_hash.py`
**Description:**
- Demonstrates integer frequency counting using a dictionary (hash map) for integers.

**Problem Solved:**
- Given a list of integers (possibly with a large or unknown range), count the frequency of each integer and answer queries about the frequency of any integer.

**Logic Summary:**
- Uses a dictionary where the key is the integer value. For each integer, increments the count in the dictionary. Querying is done using the dictionary's `get` method for O(1) access.

---

## 5. `high_low_freqmap.py`
**Description:**
- Finds the highest and lowest frequency of elements in an integer array using a hash map.

**Problem Solved:**
- Given a list of integers, determine which frequency is the highest and which is the lowest among all unique elements.

**Logic Summary:**
- Builds a frequency dictionary for the array. Iterates through the values to find the maximum and minimum frequency without using built-in min/max functions.

---

Each file is self-contained and can be run directly. Input is taken from the user, and results are printed as output. Comments in each file explain the logic and steps in detail.
