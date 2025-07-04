class Solution:
    @staticmethod
    def mathOperation(op, n1, n2):
        # Use match-case to perform the selected operation
        match op:
            case '+':
                return n1 + n2  # Addition
            case '-':
                return n1 - n2  # Subtraction
            case '*':
                return n1 * n2  # Multiplication
            case '//':
                return n1 // n2  # Integer Division
        return "Invalid Operation"  # If operation is not recognized

# Take user input for the operation and numbers
operation = input("enter your operation:")
num1 = int(input("enter the number1:"))
num2 = int(input("enter the number2:"))
# Call the function to perform the operation and print the result
result = Solution.mathOperation(operation, num1, num2)
print("Result:", result)    