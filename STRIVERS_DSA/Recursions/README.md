# Recursion Problems in Python

This folder contains Python implementations of classic recursion problems. Each file demonstrates a different recursive technique, with clear code and explanations. Below is a description of each file, the problem it solves, a summary of the logic used, and an example output where appropriate.

---

## 1. `factorial.py`
**Description:**
- Calculates the factorial of a number using recursion.

**Problem Solved:**
- Given n, compute n! (n factorial).

**Logic Summary:**
- Base case: factorial of 0 or 1 is 1. Otherwise, n * factorial(n-1).

**Example:** (n = 5)
```
120
```

---

## 2. `fibonacci.py`
**Description:**
- Computes the nth Fibonacci number using recursion.

**Problem Solved:**
- Given n, print the nth Fibonacci number.

**Logic Summary:**
- Base cases: fibonacci(0) = 0, fibonacci(1) = 1. Otherwise, fibonacci(n-1) + fibonacci(n-2).

**Example:** (n = 6)
```
8
```

---

## 3. `palindrome.py`
**Description:**
- Checks if a string is a palindrome using recursion.

**Problem Solved:**
- Given a string, determine if it reads the same forwards and backwards.

**Logic Summary:**
- Base case: if start >= end, it's a palindrome. Otherwise, compare characters at start and end, and recurse inward.

**Example:** (input = "madam")
```
is a palindrome
```

---

## 4. `Print_1_to_N.py`
**Description:**
- Prints numbers from 1 to N using recursion.

**Problem Solved:**
- Given n, print numbers from 1 to n in order.

**Logic Summary:**
- Recursively print numbers up to n-1, then print n.

**Example:** (n = 5)
```
1 2 3 4 5
```

---

## 5. `print_N_times.py`
**Description:**
- Prints a string N times using recursion.

**Problem Solved:**
- Given n and a string, print the string n times.

**Logic Summary:**
- Base case: if n == 0, stop. Otherwise, print and recurse with n-1.

**Example:** (n = 3, string = "hello")
```
hello
hello
hello
```

---

## 6. `print_n_to_1.py`
**Description:**
- Prints numbers from N to 1 using recursion.

**Problem Solved:**
- Given n, print numbers from n down to 1.

**Logic Summary:**
- Print n, then recursively print down to 1.

**Example:** (n = 5)
```
5 4 3 2 1
```

---

## 7. `reverse_of_array.py`
**Description:**
- Reverses an array using recursion.

**Problem Solved:**
- Given an array, reverse its elements in place.

**Logic Summary:**
- Swap elements at start and end, then recurse inward.

**Example:** (input = 1 2 3 4 5)
```
[5, 4, 3, 2, 1]
```

---

## 8. `sum_of_n_no's.py`
**Description:**
- Calculates the sum of the first n natural numbers using recursion.

**Problem Solved:**
- Given n, compute 1 + 2 + ... + n.

**Logic Summary:**
- Base case: if n == 0, return 0. Otherwise, n + sum(n-1).

**Example:** (n = 5)
```
15
```

Each file is self-contained and can be run directly. Input is taken from the user, and results are printed as output. Comments in each file explain the logic and steps in detail.
