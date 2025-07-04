# Pattern 18: Print a triangle of letters in reverse order, each row with the same letter
class Solution:
    @staticmethod
    def pattern18(n):
        # Loop through each row
        for i in range(n):
            # Print the same letter in each row, starting from the end
            for j in range(i+1):
                print(chr(65+n-i-1), end=" ")
            print()  # Newline after each row

n = int(input("Enter n: "))
Solution.pattern18(n)