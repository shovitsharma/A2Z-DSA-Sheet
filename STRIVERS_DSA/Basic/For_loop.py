class Solution:
    @staticmethod
    def squarenum(n):
        # Loop from 1 to n (inclusive)
        for i in range(1, n+1):
            x = i**2  # Calculate the square of i
            print(x)  # Print the square
        return

# Take user input for the number of squares to print
num = int(input())
# Call the function to print squares from 1 to num
Solution.squarenum(num)