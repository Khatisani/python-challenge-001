
"""
Function that ccurately identifies whether the bracket structure in the given string is valid.

Args:
A string

Return:
True if brackets are properly matched
False if there are extra or missing brackets 

"""

def bracket_validator(string):
    if not isinstance(string, str):
        raise ValueError
    if string == "":
        return True
    
    brackets = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in bracket_pairs.values():
            brackets.append(char)
        elif char in bracket_pairs:
            if not brackets:
                return False
            if bracket_pairs[char] != brackets.pop():
                return False
        
    return not brackets

    