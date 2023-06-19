from functions import is_number

def addEndBraceAfterParenthesis(text, curr, length):
    count = 1
    
    # Increment counter if an open parenthesis is found
    # Decrement counter if a closing parenthesis is found
    # curr will end up at the closing parenthesis
    # that matches the starting open parenthesis
    while count > 0 and curr < length:
        if text[curr] == '(':
            count += 1
        elif text[curr] == ')':
            count -= 1

        curr += 1
        
    # Add '}' after the closing parenthesis
    if curr == length:
        text.append('}')
    else:
        text.insert(curr, '}')
        
    return curr - 1
        
def addEndBraceAfterNumber(text, curr, length):
    # Find end of number
    while curr < length and is_number(text[curr]):
        curr += 1
    
    # Add '}' after the number
    if curr == length:
        text.append('}')
    else:
        text.insert(curr, '}')
        
def addOpenBraceBeforeParenthesis(text, curr):
    frac = ['\\', 'f', 'r', 'a', 'c']
    count = 1
    
    # Decrement counter if an open parenthesis is found
    # Increment counter if a closing parenthesis is found
    # curr will end up at the open parenthesis
    # that matches the starting closing parenthesis
    while count > 0 and curr >= 0:
        if text[curr] == '(':
            count -= 1
        elif text[curr] == ')':
            count += 1

        curr -= 1
        
    # Add '{' before the open parenthesis
    if curr < 0:
        text.insert(0, '{')
        for char in reversed(frac):
            text.insert(0, char)
    else:
        text.insert(curr, '{')
        for char in reversed(frac):
            text.insert(curr, char)
            
    return curr + 1
            
def addOpenBraceBeforeNumber(text, curr):
    frac = ['\\', 'f', 'r', 'a', 'c']
    
    # Find beginning of number
    while curr >= 0 and is_number(text[curr]):
        curr -= 1
    
    # Add '{' before the number
    if curr < 0:
        text.insert(0, '{')
        for char in reversed(frac):
            text.insert(0, char)
    else:
        text.insert(curr, '{')
        for char in reversed(frac):
            text.insert(curr, char)