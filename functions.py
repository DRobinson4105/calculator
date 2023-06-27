import math
from helpers import *

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def char_type(c):
    if is_number(c) or c == '.':
        return 'n'
    if c.isalpha():
        return 'a'
    if c == '(' or c == ')':
        return 'p'
    return 'o'

# Function that takes in equation as an array of tokens and
# solves all operations in equation, returning the result
def solve(expression):
    try:
        # Remove all spaces
        expression = str(expression)
        expression = expression.replace(" ", "")

        parts = []
        start = 0

        # Adds all terms and operations from the input to the array
        for i in range(len(expression)):
            if char_type(expression[i]) != char_type(expression[start]):
                if is_number(expression[start:i]):
                    parts += [float(expression[start:i])]
                else:
                    parts += [expression[start:i]]

                start = i

        # Adds last term
        if is_number(expression[start:len(expression)]):
            parts += [float(expression[start:len(expression)])]
        else:
            parts += [expression[start:len(expression)]]

        # Wraps whole equation in parenthesis
        parts.insert(0, '(')
        parts.append(')')

        # Solves and returns result
        before = []
        after = []
        found = 1

        # While there is still a parenthesis in the array
        # so part of the equation has not been solved
        while found == 1:
            found = 0

            # Find subarray of first set of parenthesis
            for i in range(len(parts)):
                if parts[i] == ')':
                    found = 1
                    end = i

                    # Find the start of the subarray
                    for j in range(end - 1, -1, -1):
                        if parts[j] == '(':
                            start = j + 1
                            break

                    # Save elements before and after subarray
                    before = parts[:start - 1]
                    after = parts[end + 1:]

                    # Solve all operations on expression in subarray
                    solvedSubarray = parts[start:end]
                    solvedSubarray = checkNegatives(solvedSubarray)
                    solvedSubarray = solveLogarithms(solvedSubarray)
                    solvedSubarray = solveSquareRoots(solvedSubarray)
                    solvedSubarray = solveFactorials(solvedSubarray)
                    solvedSubarray = solveExponents(solvedSubarray)
                    solvedSubarray = solveMultDiv(solvedSubarray)
                    solvedSubarray = solveAddSub(solvedSubarray)

                    # Recreate array using the three subarrays
                    parts = before + solvedSubarray + after
                    break

        # Only term left is answer
        if is_number(parts[0]):
            return round(parts[0], 5)
        else:
            return ""

    # If calculation failed
    except:
        return ""

def solveLogarithms(arr):
    curr = len(arr) - 1

    # Iterate through array looking for logarithms
    while curr >= 0:
        if arr[curr] == 'log' or arr[curr] == 'ln':

            # If user inputed a base
            if arr[curr + 1] == '_':
                arr[curr + 3] = math.log(arr[curr + 3]) / math.log(arr[curr + 2])

                # Remove used tokens
                for i in range(3): arr.pop(curr)

            else:
                arr[curr + 1] = math.log(arr[curr + 1])

                # If not natural log
                if arr[curr] == 'log':
                    arr[curr + 1] /= math.log(10)

                # Removed used token
                arr.pop(curr)

        curr -= 1

    # Return array with all logarithms solved
    return arr

def solveSquareRoots(arr):
    curr = len(arr) -1

    # Iterate through array looking for square roots
    while curr >= 0:
        if arr[curr] == 'sqrt':
            arr[curr + 1] = math.sqrt(arr[curr + 1])

            # Remove used token
            arr.pop(curr)

        curr -= 1

    # Return array with all square roots solved
    return arr

def checkNegatives(arr):
    curr = len(arr) - 1

    # Iterate through array looking for positive and negative number symbols
    while curr >= 0:
        if ((curr == 0 or (not is_number(arr[curr - 1]) and arr[curr - 1] != '!' and arr[curr - 1] != ')')) and (arr[curr] == '+' or arr[curr] == '-')):
            # If number needs to be converted to negative
            if (arr[curr] == '-'):
                arr[curr + 1] *= -1

            # Remove sign
            arr.pop(curr)

        # Move to next token
        curr -= 1

    # Return array with all positive and negative symbols removed
    return arr

def solveFactorials(arr):
    curr = len(arr) - 1

    # Iterate through array looking for factorials
    while curr >= 0:
        if(arr[curr] == '!'):
            # Calculate factorial
            sum = 1
            for num in range(2, int(arr[curr - 1]) + 1):
                sum *= num

            # Remove both the number and the factorial for the result
            arr[curr] = sum
            arr.pop(curr - 1)

        # Move to next token
        curr -= 1

    # Return array with all factorials solved
    return arr

def solveExponents(arr):
    curr = len(arr) - 1

    # Iterate through array looking for exponents
    while curr >= 0:
        if arr[curr] == '^':
            # Solve exponent and replace base number with result
            arr[curr - 1] = pow(float(arr[curr - 1]), float(arr[curr + 1]))

            # Remove other tokens used in operation
            arr.pop(curr)
            arr.pop(curr)

        # Move to next token
        curr -= 1

    # Return array with all exponents solved
    return arr

def solveMultDiv(arr):
    length = len(arr)
    curr = length - 1

    # Iterate through array looking for multiplication and division
    while curr >= 0:
        if arr[curr] == '*' or arr[curr] == '/':
            # Solve multiplication or division and replace first number with result
            if arr[curr] == '*':
                arr[curr - 1] = float(arr[curr - 1]) * float(arr[curr + 1])
            else:
                arr[curr - 1] = float(arr[curr - 1]) / float(arr[curr + 1])

            # Remove other tokens used in operation
            arr.pop(curr)
            arr.pop(curr)
            length -= 2

        # If two numbers are next to each other from a number
        # being next to parenthesis which implies multiplication
        elif is_number(arr[curr]) and curr < length - 1 and is_number(arr[curr + 1]):
            arr[curr] = float(arr[curr]) * float(arr[curr + 1])
            arr.pop(curr + 1)
            length -= 1

        # Move to next token
        curr -= 1

    # Return array with all multiplication and division solved
    return arr

def solveAddSub(arr):
    curr = 0
    length = len(arr)

    # Iterate through array looking for addition and subtraction
    while curr < length:
        if arr[curr] == '+' or arr[curr] == '-':
            # Solve addition or subtraction and replace first number with result
            if arr[curr] == '+':
                arr[curr - 1] = float(arr[curr - 1]) + float(arr[curr + 1])
            else:
                arr[curr - 1] = float(arr[curr - 1]) - float(arr[curr + 1])

            # Remove other tokens used in operation
            arr.pop(curr)
            arr.pop(curr)
            length -= 2

        # If current token is not addition or subtraction, move to next token
        else:
            curr += 1

    # Return array with all addition and subtraction solved
    return arr