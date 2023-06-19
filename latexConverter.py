from functions import is_number

sqrt = ['s', 'q', 'r', 't']
log = ['l', 'o', 'g']
frac = ['\\', 'f', 'r', 'a', 'c']

def convertToLaTex(text):
    text = list(text)
    text = convertSquareRoots(text)
    text = convertLogarithms(text)
    text = convertExponents(text)
    text = convertFractions(text)
    return "".join(text)
    
def convertSquareRoots(text):
    prev = text.copy()
    curr = 0
    length = len(text)
        
    while curr < length:
        try:
            if curr + 3 < length and text[curr:curr+4] == sqrt:
                # If the user has only typed sqrt, display sqrt
                if curr + 4 == length:
                    return text

                # Add '\' before and '{' after the sqrt
                text.insert(curr, '\\')
                text.insert(curr + 5, '{')
                length += 2

                # Track the number of open sets of parenthesis at tmp
                # Start tmp at the first character after '{'
                count = 1
                tmp = curr + 7

                # Increment counter if an open parenthesis is found
                # Decrement counter if a closing parenthesis is found
                # tmp will end up at the closing parenthesis that matches the starting open parenthesis
                while count > 0 and tmp < length:
                    if text[tmp] == '(':
                        count += 1
                    elif text[tmp] == ')':
                        count -= 1

                    tmp += 1

                # Add '}' after the closing parenthesis
                if tmp == length:
                    text.append('}')
                else:
                    text.insert(tmp, '}')
                length += 1

                curr += 5

            curr += 1
            
        # If anything fails, return array before the error
        except:
            return prev
        
        prev = text.copy()
        
    return text
    

def convertLogarithms(text):
    prev = text.copy()
    curr = 0
    length = len(text)

    while curr < length:
        try:
            if curr + 2 < length and text[curr:curr+3] == log:
                # If the user has only typed log, display log
                if curr + 3 == length:
                    return text
                
                # Add '\' before and '{' after the sqrt
                text.insert(curr, '\\')
                text.insert(curr + 4, '{')
                length += 2
                
                # Track the number of open sets of parenthesis at tmp
                # Start tmp at the first character after '{'
                count = 1
                tmp = curr + 6

                # Increment counter if an open parenthesis is found
                # Decrement counter if a closing parenthesis is found
                # tmp will end up at the closing parenthesis that matches the starting open parenthesis
                while count > 0 and tmp < length:
                    if text[tmp] == '(':
                        count += 1
                    elif text[tmp] == ')':
                        count -= 1
                        
                    tmp += 1
                        
                # Add '}' after the closing parenthesis
                if tmp == length:
                    text.append('}')
                else:
                    text.insert(tmp, '}')
                length += 1

                curr += 4

            curr += 1
            
        # If anything fails, return array before the error
        except:
            return prev
        
        prev = text.copy()
            
    return text

def convertExponents(text):
    prev = text.copy()
    curr = 0
    length = len(text)

    while curr < length:
        # If the user has not typed the power yet
        if text[curr] == '^' and curr == length - 1:
            return text[:-1]
        
        try:
            # If exponent is found and the power has multiple characters
            if text[curr] == '^' and not (is_number(text[curr + 1]) and (curr + 2 == length or not is_number(text[curr + 2]))):
                # Add '{' after the ^
                text.insert(curr + 1, '{')
                length += 1

                # Track the number of open sets of parenthesis at tmp
                # Start tmp at the first character after '{'
                count = 1
                tmp = curr + 2

                # Keep option at 0 if power is just a number
                option = 0
                if text[tmp] == '(':
                    option = 1
                    tmp += 1

                # If power was just a number, find end of number
                if option == 0:
                    while tmp < length and is_number(text[tmp]):
                        tmp += 1
                        
                # Increment counter if an open parenthesis is found
                # Decrement counter if a closing parenthesis is found
                # tmp will end up at the closing parenthesis
                # that matches the starting open parenthesis
                else:
                    while count > 0 and tmp < length:
                        if text[tmp] == '(':
                            count += 1
                        elif text[tmp] == ')':
                            count -= 1

                        tmp += 1

                # Add '}' after the closing parenthesis or number
                if tmp == length:
                    text.append('}')
                else:
                    text.insert(tmp, '}')

                length += 1

            curr += 1

        # If anything fails, return array before the error
        except:
            return prev

        prev = text.copy()

    return text

def convertFractions(text):
    prev = text.copy()
    curr = 0
    length = len(text)
    
    while curr < length:
        try:
            # If fraction is found
            if text[curr] == '/':
                text.insert(curr + 1, '{')
                text.insert(curr, '}')
                length += 2
                
                count = 1
                tmp = curr - 1
                
                option = 0
                if text[tmp] == ')':
                    option = 1
                    tmp -= 1
                
                if option == 0:
                    while tmp >= 0 and is_number(text[tmp]):
                        tmp -= 1
                        
                else:
                    while count > 0 and tmp >= 0:
                        if text[tmp] == '(':
                            count -= 1
                        elif text[tmp] == ')':
                            count += 1
                            
                        tmp -= 1
                        
                if tmp < 0:
                    text.insert(0, '{')
                    for char in reversed(frac):
                        text.insert(0, char)
                else:
                    text.insert(tmp, '{')
                    for char in reversed(frac):
                        text.insert(0, char)
                    
                length += 5
                curr += 7
                text.pop(curr)
                
                count = 1
                tmp = curr + 1
                
                option = 0
                if text[tmp] == '(':
                    option = 1
                    tmp += 1
                    
                if option == 0:
                    while tmp < length and is_number(text[tmp]):
                        tmp += 1
                        
                else:
                    while count > 0 and tmp < length:
                        if text[tmp] == '(':
                            count += 1
                        elif text[tmp] == ')':
                            count -= 1
                            
                        tmp += 1
                        
                if tmp == length:
                    text.append('}')
                else:
                    text.insert(tmp, '}')
                    
                length += 1
                
            curr += 1
        
        except:
            return prev

        prev = text.copy()
        
    return text