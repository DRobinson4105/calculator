def solve(arr):

    before = []
    after = []

    found = 1
    while found == 1:

        found = 0
        for i in range(len(arr)):

            if arr[i] == ')':

                found = 1
                end = i

                for j in range(end - 1,-1,-1):

                    if arr[j] == '(':

                        start = j + 1
                        break

                before = arr[:start - 1]
                after = arr[end + 1:]
                temp = arr[start:end]
                temp = solveAll(temp)
                arr = before + temp + after

                break

    arr = solveAll(arr)
    return arr
    
def solveFactorials(arr):

    for curr in range(len(arr) - 1, -1, -2):

        if(arr[curr][-1] == '!'):

            sum = 1

            for num in range(2, int(arr[curr][:-1]) + 1):
                sum *= num                      

            arr[curr] = str(sum)

    return arr

def solveExponents(arr):

    for curr in range(len(arr) - 2, 0, -2):

        if arr[curr] == '^':

            arr[curr - 1] = str(pow(float(arr[curr - 1]), float(arr[curr + 1])))
            arr.pop(curr)
            arr.pop(curr)

    return arr

def solveMultDiv(arr):

    curr = 1
    while curr < len(arr):
        if arr[curr] == '*' or arr[curr] == '/':
            if arr[curr] == '*':
                arr[curr - 1] = str(float(arr[curr - 1]) * float(arr[curr + 1]))
            else:
                arr[curr - 1] = str(float(arr[curr - 1]) / float(arr[curr + 1]))

            arr.pop(curr)
            arr.pop(curr) 

        else:
            curr += 2

    return arr

def solveAddSub(arr):

    curr = 1
    while curr < len(arr):

        if arr[curr] == '+' or arr[curr] == '-':

            if arr[curr] == '+':
                arr[curr - 1] = str(float(arr[curr - 1]) + float(arr[curr + 1]))
            else:
                arr[curr - 1] = str(float(arr[curr - 1]) - float(arr[curr + 1]))

            arr.pop(curr)
            arr.pop(curr)

        else:
            curr += 2
    
    return arr

def solveAll(arr):
    
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
    
    match option:
        case '0':
            print("Thank you for using the calculator!")
        case '1':
            try:
                expression = input('What would you like to calculate: ')
                expression = expression.replace(" ", "") #removes all spaces

                parts = []
                start = 0

                # Adds all terms and operations from the input to the array
                for i in range(len(expression)): 

                    if expression[i] == '+' or expression[i] == '-' or expression[i] == '*' or expression[i] == '/' or expression[i] == '^' or expression[i] == '(' or expression[i] == ')':
                        if(i != start):
                            parts += [expression[start:i]]
                        parts += [expression[i]]
                        start = i + 1

                if parts[-1] != ')':
                    parts += [expression[start:len(expression)]]
                
                parts = solve(parts)
                print('The answer is', parts[0])

            except:
                print('Could not solve this')

        case _:
            print("That is an invalid option")
