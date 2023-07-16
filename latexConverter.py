from functions import is_number
from helpers import *

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
                # If the user has only typed sqrt or there
                # is not an open parenthesis after sqrt
                if curr + 4 == length or text[curr + 4] != '(':
                    return text

                # Add '\' before and '{' after the sqrt, replacing the start parenthesis of sqrt
                text.insert(curr, '\\')                
                text[curr + 5] = '{'
                length += 1

                # Replace end parenthesis of sqrt with end brace
                tmp = findEndParenthesis(text, curr + 7, length)
                
                # Replace closing parenthesis with '}'
                if tmp == length - 1:
                    text.append('}')
                else:
                    text.insert(tmp + 1, '}')
                
                text.pop(tmp)
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

                # Add '\' before the log
                text.insert(curr, '\\')
                length += 1
                curr += 4

                # If log base was given
                if text[curr] == '_':
                    # Add '{' before base
                    text.insert(curr + 1, '{')
                    length += 1

                    # Find end of base
                    if text[curr + 2] == '(':
                        pos = findEndParenthesis(text, curr + 3, length)
                    else:
                        pos = findEndNumber(text, curr + 2, length)

                    print(text[pos])

                    # Add '}' after the closing parenthesis
                    if pos == length - 1:
                        text.append('}')
                    else:
                        text.insert(pos + 1, '}')
                    length += 1

                    # Move curr to after base
                    curr = pos + 2

                # Save base
                prev = text.copy()
                print(text)

                # Add '{' after base and log
                text.insert(curr, '{')
                length += 1

                # Add end brace after all open parenthesis have been
                # closed starting at the first character after '{'
                tmp = findEndParenthesis(text, curr + 3, length)

                # Add '}' after the closing parenthesis
                if tmp == length - 1:
                    text.append('}')
                else:
                    text.insert(tmp + 1, '}')

                length += 1
                curr = tmp + 1

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

                # If power starts with a parenthesis, add end
                # brace after all open parenthesis have been
                # closed starting at the first character after '{'
                if text[curr + 2] == '(':
                    tmp = findEndParenthesis(text, curr + 2, length)
                    
                    # Add '}' after the closing parenthesis
                    if tmp == length - 1:
                        text.append('}')
                    else:
                        text.insert(tmp + 1, '}')

                # If power was just a number, find end of number
                else:
                    tmp = findEndNumber(text, curr + 3, length)
                    
                    # Add '}' after the number
                    if tmp == length - 1:
                        text.append('}')
                    else:
                        text.insert(tmp + 1, '}')

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

                # If numerator ends with a parenthesis, add open
                # brace after all open parenthesis have been
                # closed starting at the first character after '}'
                if text[curr - 1] == ')':
                    tmp = findStartParenthesis(text, curr - 2)
                    
                    # Add '{' before the open parenthesis
                    if tmp < 0:
                        text.insert(0, '{')
                        for char in reversed(frac):
                            text.insert(0, char)
                    else:
                        text.insert(tmp, '{')
                        for char in reversed(frac):
                            text.insert(tmp, char)

                # If power was just a number, find end of number
                else:
                    tmp = findStartNumber(text, curr - 1)
                    
                    # Add '{' before the number
                    if tmp < 0:
                        text.insert(0, '{')
                        for char in reversed(frac):
                            text.insert(0, char)
                    else:
                        text.insert(tmp, '{')
                        for char in reversed(frac):
                            text.insert(tmp, char)

                length += 5

                # Move curr to starting brace of denominator
                curr += 7

                # Remove fraction symbol
                text.pop(curr)

                # If denominator starts with a parenthesis, add end
                # brace after all open parenthesis have been
                # closed starting at the first character after '{'
                if text[curr + 1] == '(':
                    tmp = findEndParenthesis(text, curr + 2, length)
                    
                    # Add '}' after the closing parenthesis
                    if tmp == length - 1:
                        text.append('}')
                    else:
                        text.insert(tmp + 1, '}')

                # If power was just a number, find end of number
                else:
                    tmp = findEndNumber(text, curr + 1, length)

                    # Add '}' after the number
                    if tmp == length - 1:
                        text.append('}')
                    else:
                        text.insert(tmp + 1, '}')
                        
                length += 1

            curr += 1

        except:
            return prev

        prev = text.copy()

    return text