# Pattern 15: Print a triangle of letters, each row with increasing letters
class Solution:
    @staticmethod
    def pattern15(n):
        # Loop through each row
        for i in range(n):
            # Print letters from 'A' up to the ith letter
            for j in range(i+1):
                print(chr(65+j), end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern15(n)