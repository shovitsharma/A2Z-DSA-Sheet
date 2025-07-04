class Solution:
    @staticmethod
    def HCF(a, b):
        # Use Euclidean algorithm to find HCF
        while b:
            a, b = b, a % b
        return a

# Take user input for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Print the HCF of the two numbers
print("HCF:", Solution.HCF(num1, num2))
