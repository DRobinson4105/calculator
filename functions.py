import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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
            if not is_number(expression[i]) and expression[i] != '.' and not expression[i].isalpha():
                if(i != start):
                    if is_number(expression[start:i]):
                        parts += [float(expression[start:i])]
                    else:
                        parts += [expression[start:i]]
                    

                parts += [str(expression[i])]
                start = i + 1

        # Adds last term
        if start != len(expression) and (len(parts) == 0 or parts[-1] != ')' or parts[-1] != '!'):
            parts += [float(expression[start:len(expression)])]

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

                    # Solve factorials and PEMDAS on equation in array
                    solvedSubarray = parts[start:end]
                    solvedSubarray = solveLogarithms(solvedSubarray)
                    solvedSubarray = checkNegatives(solvedSubarray)
                    solvedSubarray = solveFactorials(solvedSubarray)
                    solvedSubarray = solveExponents(solvedSubarray)
                    solvedSubarray = solveMultDiv(solvedSubarray)
                    solvedSubarray = solveAddSub(solvedSubarray)

                    if len(before) >= 3 and before[-2] == '_' and before[-3] == 'log':
                        solvedSubarray[0] = ' ' + str(solvedSubarray[0])
                        
                    # Recreate array using the three subarrays
                    parts = before + solvedSubarray + after
                    break

        # Only term left is answer
        if is_number(parts[0]):
            return parts[0]
        else:
            return ""

    # If calculation failed
    except:
        return ""
    
def solveLogarithms(arr):
    length = len(arr)
    curr = length - 1
    
    # Iterate through array looking for logarithms
    while curr >= 0:
        if arr[curr] == 'log' or arr[curr] == 'ln':
            if curr + 3 < length and arr[curr + 3][0] == ' ':
                arr[curr + 3] = math.log(float(arr[curr + 3][1:])) / math.log(arr[curr + 2])

                # Removed used tokens
                arr.pop(curr)
                arr.pop(curr)
                arr.pop(curr)
                length -= 3

            else:
                arr[curr + 1] = math.log(arr[curr + 1])

                # Calculate natural log if needed
                if arr[curr] == 'log':
                    arr[curr + 1] /= math.log(10)

                # Remove used number
                arr.pop(curr)
                length -= 1

        curr -= 1

    # Return array with all logarithms removed
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

    # Return array with all positive and negative removed
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
            arr[curr] = str(sum)
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
            arr[curr - 1] = str(pow(float(arr[curr - 1]), float(arr[curr + 1])))

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
                arr[curr - 1] = str(float(arr[curr - 1]) * float(arr[curr + 1]))
            else:
                arr[curr - 1] = str(float(arr[curr - 1]) / float(arr[curr + 1]))

            # Remove other tokens used in operation
            arr.pop(curr)
            arr.pop(curr)
            length -= 2

        # If two numbers are next to each other from a number
        # being next to parenthesis which implies multiplication
        elif is_number(arr[curr]) and curr < length - 1 and is_number(arr[curr + 1]):
            arr[curr] = str(float(arr[curr]) * float(arr[curr + 1]))
            arr.pop(curr + 1)
            length -= 1

        # Move to next token
        curr -= 1

    # Return array with all multiplication and division solved
    return arr

def solveAddSub(arr):
    curr = len(arr) - 1

    # Iterate through array looking for addition and subtraction
    while curr >= 0:
        if arr[curr] == '+' or arr[curr] == '-':
            # Solve addition or subtraction and replace first number with result
            if arr[curr] == '+':
                arr[curr - 1] = str(float(arr[curr - 1]) + float(arr[curr + 1]))
            else:
                arr[curr - 1] = str(float(arr[curr - 1]) - float(arr[curr + 1]))

            # Remove other tokens used in operation
            arr.pop(curr)
            arr.pop(curr)

        # If current token is not addition or subtraction, move to next token
        curr -= 1

    # Return array with all addition and subtraction solved
    return arr