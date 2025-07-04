# Pattern 13: Print a pattern of numbers in a triangle, increasing across rows
class Solution:
    @staticmethod
    def pattern13(n):
        num = 1
        # Loop through each row
        for i in range(1, n+1):
            # Print numbers in the row
            for j in range(i):
                print(num, end=" ")
                num += 1
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern13(n)