# ➗ Basic Math – A2Z DSA Sheet

This folder includes foundational mathematical problems typically encountered in the early stages of DSA preparation. These problems cover number properties, mathematical operations, and algorithmic fundamentals like HCF, prime numbers, and digit manipulation.

---

## 📄 Files & Descriptions

### 1. `armstrong.py`
**🔹 Task:** Check if a number is an **Armstrong number**.

**🧠 Logic:**
- An Armstrong number is equal to the sum of its digits each raised to the power of the number of digits.
- Converts the number to a string to easily access each digit and count them.
- Checks if the sum of powered digits equals the original number.

---

### 2. `countdigits.py`
**🔹 Task:** Count the number of digits in an integer.

**🧠 Logic:**
- Uses a `while` loop to repeatedly divide the number by 10 until it becomes 0.
- Increments a counter during each iteration to count how many times division occurs.

---

### 3. `HCF.py`
**🔹 Task:** Calculate the **HCF (Highest Common Factor)** of two numbers.

**🧠 Logic:**
- Uses the **Euclidean algorithm**:
  - Repeatedly replace `a` with `b`, and `b` with `a % b`, until `b` becomes 0.
  - The final value of `a` is the HCF.

---

### 4. `prime.py`
**🔹 Task:** Check whether a number is **prime**.

**🧠 Logic:**
- A number is prime if it’s greater than 1 and has no divisors other than 1 and itself.
- Loops from 2 to `sqrt(n)` to check for any divisors.
- Returns `True` if no divisors are found, `False` otherwise.

---

### 5. `print_all_divisor.py`
**🔹 Task:** Print **all divisors** of a given number.

**🧠 Logic:**
- Loops from 1 to `n`, and for each number `i`, prints it if `n % i == 0`.

---

## 🚀 Notes

- These are key building blocks for later DSA problems.
- Helps in understanding loops, conditions, and number theory basics.
- Good practice for interview warm-ups and entrance test problems.

📁 _Next: You could optimize divisor printing by looping only till sqrt(n) and using pairs for efficiency._