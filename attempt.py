from collections  import Counter

"""
This was my attempt at solving it without going the stack route
I tried to be smart and crative for a few hours
I finally made peace with it that I have to use stack :(

"""

def attempt_bracket_validator(string):
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

        







