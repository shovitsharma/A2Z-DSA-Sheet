# Pattern 12: Print a pattern with numbers increasing, spaces, then numbers decreasing
class solution:
    @staticmethod
    def pattern12(n):
        # Loop through each row
        for i in range(1, n+1):
            # Print numbers from 1 to i
            for j in range(1, i+1):
                print(j, end="")
            # Print spaces in the middle
            space = 2 * (n - i)
            print(" " * space, end="")
            # Print numbers from i down to 1
            for j in range(i, 0, -1):
                print(j, end="")
            print()  # Newline after each row

num = int(input())
solution.pattern12(num)