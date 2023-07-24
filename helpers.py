def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def findEndParenthesis(text, curr, length):
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

    return curr - 1

def findEndNumber(text, curr, length):
    # Find end of number
    while curr < length and is_number(text[curr]):
        curr += 1

    return curr - 1

def findStartParenthesis(text, curr):
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

    return curr + 1

def findStartNumber(text, curr):
    # Find beginning of number
    while curr >= 0 and is_number(text[curr]):
        curr -= 1

    return curr + 1

def char_type(c):
    if is_number(c) or c == '.':
        return 'n'
    if c.isalpha():
        return 'a'
    if c == '(' or c == ')':
        return 'p'
    if c == '+' or c == '-' or c == '*' or c == '/' or c == '!' or c == '^' or c == '_':
        return 'o'

    return 'e'

def validWords(text):
    return text == 'pi' or text == 'log' or text == 'sqrt'