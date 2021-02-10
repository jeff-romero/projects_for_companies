# Jeffrey Romero
# 2/10/2021

# Can mirror one word or a complete sentence if sentence is put into quotes: "sentence_goes_here".

import sys


def pop_from_stack(stack):
    returnString = ""
    for i in range(len(stack)):
        returnString += stack.pop()

    return returnString


if len(sys.argv) > 1:
    ret = ""
    input_string = sys.argv[1]
    char_stack = []
    for i in input_string:
        if i != " ":
            char_stack.append(i)
        else:
            ret += pop_from_stack(char_stack)
            ret += " "

    ret += pop_from_stack(char_stack)

    print("Mirrored string: " + ret + "\n")
else:
    print("Error - Usage: " + sys.argv[0] + " enter_string\n")
    exit
