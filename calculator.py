# Function that takes in equation as an array of tokens and
# solves all operations in equation, returning the result
def solve(arr):
    before = []
    after = []
    found = 1

    # While there is still a parenthesis in the array
    # so part of the equation has not been solved
    while found == 1:
        found = 0

        # Find subarray of first set of parenthesis
        for i in range(len(arr)):
            if arr[i] == ')':
                found = 1
                end = i

                # Find the start of the subarray
                for j in range(end - 1, -1, -1):
                    if arr[j] == '(':
                        start = j + 1
                        break
                
                # Save elements before and after subarray
                before = arr[:start - 1]
                after = arr[end + 1:]

                # Solve subarray 
                solvedSubarray = arr[start:end]
                solvedSubarray = solveAll(solvedSubarray)

                # Recreate array using the three subarrays
                arr = before + solvedSubarray + after
                break
    
    # Only term left is answer
    return arr[0]
    
def solveFactorials(arr):
    curr = 0
    length = len(arr)

    # Iterate through array looking for factorials
    while curr < length:
        if(arr[curr] == '!'):
            # Calculate factorial
            sum = 1
            for num in range(2, int(arr[curr - 1]) + 1):
                sum *= num                      

            # Remove both the number and the factorial for the result
            arr[curr] = str(sum)
            arr.pop(curr - 1)
            length -= 1
        
        # If current token is not a factorial, move to next token
        else:
            curr += 1

    # Return array with all factorials solved
    return arr

def solveExponents(arr):
    curr = 1
    length = len(arr)

    # Iterate through array looking for exponents
    while curr < length:
        if arr[curr] == '^':
            # Solve exponent and replace base number with result
            arr[curr - 1] = str(pow(float(arr[curr - 1]), float(arr[curr + 1])))

            # Remove other tokens used in operation
            arr.pop(curr)
            arr.pop(curr)
            length -= 2

        # If curent token is not an exponent, move to next token
        else:
            curr += 1

    # Return array with all exponents solved
    return arr

def solveMultDiv(arr):
    curr = 0
    length = len(arr)

    # Iterate through array looking for multiplication and division
    while curr < length:
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

        # If current token is not multiplication or division, move to next token
        else:
            curr += 1

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
                arr[curr - 1] = str(float(arr[curr - 1]) + float(arr[curr + 1]))
            else:
                arr[curr - 1] = str(float(arr[curr - 1]) - float(arr[curr + 1]))

            # Remove other tokens used in operation
            arr.pop(curr)
            arr.pop(curr)
            length -= 2

        # If current token is not addition or subtraction, move to next token
        else:
            curr += 1
    
    # Return array with all addition and subtraction solved
    return arr

def solveAll(arr):
    # Solve factorials and PEMDAS on equation in array
    arr = solveFactorials(arr)
    arr = solveExponents(arr)
    arr = solveMultDiv(arr)
    arr = solveAddSub(arr)
    return arr

option = -1
while(option != '0'):

    print("Calculator Functions:")
    print("0) Exit")
    print("1) Calculate")
    option = input("Option: ")
    option = option.replace(" ", "")
    
    match option:
        # User is exiting the calculator
        case '0':
            print("Thank you for using the calculator!")

        # User wants to calculate an equation
        case '1':
            try:
                expression = input("What would you like to calculate: ")

                # Remove all spaces
                expression = expression.replace(" ", "")

                parts = []
                start = 0

                # Adds all terms and operations from the input to the array
                for i in range(len(expression)): 

                    if expression[i] == '+' or expression[i] == '-' or expression[i] == '*' or expression[i] == '/':
                        if expression[i] == '^' or expression[i] == '(' or expression[i] == ')' or expression[i] == '!':
                            if(i != start):
                                parts += [str(expression[start:i])]

                            parts += [str(expression[i])]
                            start = i + 1

                # Adds last term
                if parts[-1] != ')' or parts[-1] != '!':
                    parts += [expression[start:len(expression)]]

                # Wraps whole equation in parenthesis
                parts.insert(0, '(')
                parts.append(')')

                # Solves and prints result
                parts = solve(parts)
                print('The answer is', parts)

            # If calculation failed
            except:
                print('Could not solve this')

        # Invalid input
        case _:
            print("That is an invalid option")
