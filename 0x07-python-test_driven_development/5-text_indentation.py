#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # index = text.find("($.,?:)")
    ss = "$.?:"
    for c in text:
        # if (c == '$' or c == '.' or c == ',' or c == '?' or c == ':'):
        
        if not (c in ss):
            print(c, end="")
        else:
            print(c, end="$\n")
            print("$")
