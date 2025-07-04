# Pattern 16: Print a triangle of letters in reverse order
class Solution:
    @staticmethod
    def pattern16(n):
        # Loop through each row
        for i in range(n):
            # Print letters from the ith letter down to 'A'
            for j in range(i, -1, -1):
                print(chr(65+j), end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern16(n)