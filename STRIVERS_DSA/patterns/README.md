# Pattern Problems in Python

This folder contains Python implementations of classic pattern printing problems. Each file demonstrates a different pattern, with clear code and explanations. Below is a description of each file, the problem it solves, a summary of the logic used, and an example output for each pattern.

---

## 1. `pattern1.py`
**Description:**
- Prints a square of stars.

**Problem Solved:**
- Given n, print an n x n square of stars.

**Logic Summary:**
- Uses two nested loops: the outer loop for rows and the inner loop for columns.

**Example:** (n = 3)
```
* * *
* * *
* * *
```

---

## 2. `pattern2.py`
**Description:**
- Prints a right-angled triangle of stars.

**Problem Solved:**
- Given n, print a triangle with n rows, each row containing one more star than the previous.

**Logic Summary:**
- Outer loop for rows, inner loop prints increasing number of stars per row.

**Example:** (n = 4)
```
*
* *
* * *
* * * *
```

---

## 3. `pattern3.py`
**Description:**
- Prints a right-angled triangle of numbers, each row starting from 1 up to the row number.

**Problem Solved:**
- Given n, print a triangle with numbers increasing in each row.

**Logic Summary:**
- Outer loop for rows, inner loop prints numbers from 1 to i.

**Example:** (n = 4)
```
1
1 2
1 2 3
1 2 3 4
```

---

## 4. `pattern4.py`
**Description:**
- Prints a right-angled triangle where each row contains the row number.

**Problem Solved:**
- Given n, print a triangle with each row filled with its row number.

**Logic Summary:**
- Outer loop for rows, inner loop prints the row number i times.

**Example:** (n = 4)
```
1
2 2
3 3 3
4 4 4 4
```

---

## 5. `pattern5.py`
**Description:**
- Prints an inverted right-angled triangle of stars.

**Problem Solved:**
- Given n, print a triangle with n stars in the first row, decreasing by one each row.

**Logic Summary:**
- Outer loop for rows, inner loop prints decreasing number of stars.

**Example:** (n = 4)
```
* * * *
* * *
* *
*
```

---

## 6. `pattern6.py`
**Description:**
- Prints an inverted right-angled triangle of numbers.

**Problem Solved:**
- Given n, print a triangle with numbers decreasing in each row.

**Logic Summary:**
- Outer loop for rows, inner loop prints numbers from 1 to i.

**Example:** (n = 4)
```
1 2 3 4
1 2 3
1 2
1
```

---

## 7. `pattern7.py`
**Description:**
- Prints a pyramid of stars aligned to the center.

**Problem Solved:**
- Given n, print a centered pyramid of stars.

**Logic Summary:**
- Outer loop for rows, inner loop prints spaces and stars to form a pyramid.

**Example:** (n = 4)
```
   *
  ***
 *****
*******
```

---

## 8. `pattern8.py`
**Description:**
- Prints an inverted pyramid of stars aligned to the center.

**Problem Solved:**
- Given n, print a centered inverted pyramid of stars.

**Logic Summary:**
- Outer loop for rows, inner loop prints spaces and stars to form an inverted pyramid.

**Example:** (n = 4)
```
*******
 *****
  ***
   *
```

---

## 9. `pattern9.py`
**Description:**
- Prints a diamond of stars.

**Problem Solved:**
- Given n, print a diamond shape using stars.

**Logic Summary:**
- Combines a pyramid and an inverted pyramid.

**Example:** (n = 4)
```
   *
  ***
 *****
*******
 *****
  ***
   *
```

---

## 10. `pattern10.py`
**Description:**
- Prints a right-angled triangle and its mirror image.

**Problem Solved:**
- Given n, print a triangle and its mirror image below.

**Logic Summary:**
- First part increases stars, second part decreases stars.

**Example:** (n = 4)
```
*
* *
* * *
* * * *
* * *
* *
*
```

---

## 11. `pattern11.py`
**Description:**
- Prints a binary triangle pattern.

**Problem Solved:**
- Given n, print a triangle with alternating 1s and 0s.

**Logic Summary:**
- Uses (i+j)%2 to alternate between 1 and 0.

**Example:** (n = 4)
```
1
0 1
1 0 1
0 1 0 1
```

---

## 12. `pattern12.py`
**Description:**
- Prints a pattern with numbers increasing, spaces, then numbers decreasing.

**Problem Solved:**
- Given n, print a pattern with numbers increasing, spaces, then numbers decreasing in each row.

**Logic Summary:**
- Outer loop for rows, inner loops for numbers and spaces.

**Example:** (n = 4)
```
1      1
1 2    2 1
1 2 3  3 2 1
1 2 3 4 4 3 2 1
```

---

## 13. `pattern13.py`
**Description:**
- Prints a triangle of numbers increasing across rows.

**Problem Solved:**
- Given n, print a triangle with numbers increasing across rows.

**Logic Summary:**
- Uses a counter variable to print increasing numbers.

**Example:** (n = 4)
```
1
2 3
4 5 6
7 8 9 10
```

---

## 14. `pattern14.py`
**Description:**
- Prints a triangle of letters, each row with the same letter.

**Problem Solved:**
- Given n, print a triangle with each row containing the same letter.

**Logic Summary:**
- Uses chr(65+i) to print letters.

**Example:** (n = 4)
```
A
B B
C C C
D D D D
```

---

## 15. `pattern15.py`
**Description:**
- Prints a triangle of letters, each row with increasing letters.

**Problem Solved:**
- Given n, print a triangle with letters increasing in each row.

**Logic Summary:**
- Uses chr(65+j) to print letters.

**Example:** (n = 4)
```
A
A B
A B C
A B C D
```

---

## 16. `pattern16.py`
**Description:**
- Prints a triangle of letters in reverse order.

**Problem Solved:**
- Given n, print a triangle with letters in reverse order in each row.

**Logic Summary:**
- Uses chr(65+j) in reverse order.

**Example:** (n = 4)
```
A
B A
C B A
D C B A
```

---

## 17. `pattern17.py`
**Description:**
- Prints a pyramid of letters.

**Problem Solved:**
- Given n, print a centered pyramid of letters.

**Logic Summary:**
- Outer loop for rows, inner loops for spaces and letters.

**Example:** (n = 4)
```
   A
  ABA
 ABCBA
ABCDCBA
```

---

## 18. `pattern18.py`
**Description:**
- Prints a triangle of letters in reverse order, each row with the same letter.

**Problem Solved:**
- Given n, print a triangle with the same letter in each row, starting from the end.

**Logic Summary:**
- Uses chr(65+n-i-1) to print letters.

**Example:** (n = 4)
```
D
C C
B B B
A A A A
```

---

## 19. `pattern19.py`
**Description:**
- Prints a diamond of stars.

**Problem Solved:**
- Given n, print a diamond shape using stars.

**Logic Summary:**
- Combines a pyramid and an inverted pyramid.

**Example:** (n = 4)
```
   *
  ***
 *****
*******
 *****
  ***
   *
```

---

## 20. `pattern20.py`
**Description:**
- Prints a hollow square of stars.

**Problem Solved:**
- Given n, print a hollow square of stars.

**Logic Summary:**
- Prints stars at the border, spaces inside.

**Example:** (n = 4)
```
****
*  *
*  *
****
```

---

## 21. `pattern21.py`
**Description:**
- Prints a hollow square of stars using string multiplication.

**Problem Solved:**
- Given n, print a hollow square using string multiplication.

**Logic Summary:**
- Uses string multiplication for borders and spaces.

**Example:** (n = 4)
```
****
*  *
*  *
****
```

---

## 22. `pattern22.py`
**Description:**
- Prints a cross (X) pattern of stars.

**Problem Solved:**
- Given n, print a cross (X) pattern using stars.

**Logic Summary:**
- Prints stars at the diagonals.

**Example:** (n = 5)
```
*   *
 * *
  *
 * *
*   *
```

---

Each file is self-contained and can be run directly. Input is taken from the user, and results are printed as output. Comments in each file explain the logic and steps in detail.
