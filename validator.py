from collections import Counter
"""
Function that ccurately identifies whether the bracket structure in the given string is valid.

Args:
A string

Return:
True if brackets are properly matched
False if there are extra or missing brackets 

"""
# string = "life(())"

def bracket_validator(string):
    if not isinstance(string, str):
        raise ValueError
    if string == "":
        return True
    opening= ["[", "(", "{"]
    closing= ["]", ")", "}"]
    matched = []
    brackets = []


    if string.count("(") == string.count(")") or string.count("[") == string.count("]") or string.count("{") == string.count("}"):
        for char in string:
            if char in opening or char in closing:
                brackets.append(char)

        if brackets[0] in opening and brackets[-1] in closing:
            for bracket, next_bracket in zip(brackets, brackets[1:]):
                if bracket in opening and next_bracket in closing:
                    matched.append(bracket)
                    matched.append(next_bracket)
                
                counter_unmatched = Counter(brackets) - Counter(matched)
                unmatched = list(counter_unmatched.elements())
        
                if not unmatched:
                    return True
        
    return False

# print(bracket_validator(string))

        







