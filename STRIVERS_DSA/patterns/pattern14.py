# Pattern 14: Print a triangle of letters, each row with the same letter
class Solution:
    @staticmethod
    def pattern14(n):
        # Loop through each row
        for i in range(n):
            # Print the same letter in each row
            for j in range(i+1):
                print(chr(65+i), end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern14(n)
