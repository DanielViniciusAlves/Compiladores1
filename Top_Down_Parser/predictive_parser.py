# Considering the expression:
# expr -> digit rest
# rest -> - digit rest
# rest -> + digit rest
# digit -> 0 | 1 | 2 | 3 ... | 9

import time

i=0
input = "1+3+5+6+2"

def expr():
    digit();
    rest();

def rest():
    if (lookAhead == "-") or (lookAhead == "+"):
        token=lookAhead
        recognize(lookAhead);
        digit();
        print(token)
        rest();
    elif (lookAhead == "Finished"):
        print("Finished!")
    else:
        error();

def digit():
    if lookAhead.isnumeric():
        print(lookAhead)
        recognize(lookAhead);
    else:
        error();

def recognize(token):
    if token == lookAhead:
        nextToken();
    else:
        error();

def error():
    print("Error Found")
    print(lookAhead)
    exit(-1)

def nextToken():
    global i, lookAhead
    i = i + 1 
    if i < len(input):
        lookAhead = input[i]
    else:
        lookAhead = "Finished"

lookAhead = input[0]
expr()
