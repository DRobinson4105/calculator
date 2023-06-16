from tkinter import *

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
            if not is_number(expression[i]):
                if(i != start):
                    parts += [float(expression[start:i])]

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
                    # Solve subarray 
                    solvedSubarray = parts[start:end]
                    solvedSubarray = solveAll(solvedSubarray)

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
    
    
def checkNegatives(arr):
    curr = 0
    length = len(arr)
    
    # Iterate through array looking for positive and negative number symbols
    while curr < length - 1:
        if ((curr == 0 or (not is_number(arr[curr - 1]) and arr[curr - 1] != '!' and arr[curr - 1] != ')')) and (arr[curr] == '+' or arr[curr] == '-')):
            # If number needs to be converted to negative
            if (arr[curr] == '-'):
                arr[curr + 1] *= -1
            
            # Remove sign
            arr.pop(curr)
            length -= 1
            
        else:
            curr += 1
    
    # Return array with all positive and negative removed
    return arr
    
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

        # If two numbers are next to each other from a number 
        # being next to parenthesis which implies multiplication
        elif curr < length - 1 and is_number(arr[curr]) and is_number(arr[curr + 1]):
            arr[curr] = str(float(arr[curr]) * float(arr[curr + 1]))
            arr.pop(curr + 1)
            length -= 1

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
    arr = checkNegatives(arr)
    arr = solveFactorials(arr)
    arr = solveExponents(arr)
    arr = solveMultDiv(arr)
    arr = solveAddSub(arr)
    return arr

def calc():
    label["text"] = solve(entry.get())

    # This will run the function in every 100ms
    master.after(100, calc)

master = Tk()

Label(master, text="Main Value").grid(row=0, sticky = E)

entry = Entry(master)

entry.grid(row=0, column=1)

label = Label(master)
label.grid(row=4, column = 1)

# Run the function and it will keep running in the background.
calc()

master.mainloop()