'''
Create a program that takes 3 inputs, a lower bound, an upper bound, and the expression.
Calculate the sum of that range based on the given expression and output result.

For Example:
Input: 2 4 *2
Output: 18 (2*2 + 3*2 + 4*2)

Input: 1 5 %2
Output: 3 (1%2 + 2%2 + 3%2 + 4%2 + 5%2)

'''

input1 = input() # Integer
input2 = input() # Integer
numb1 = int(input1)
numb2= int(input2)
input3 = input() # Special character + number  (+, -, *, /, %)
numb3 = int(input3[1])
expr = input3[0] #Expression


def SumCalc(a, b):
    if expr == '+':
        add(a, b)
    elif expr == '-':
        minus(a, b)
    elif expr == '*':
        times(a, b)
    elif expr == '/':
        div(a, b)
    elif expr == '%':
        modula(a, b)
    else:
        print('Can\'t operate the expression')
        

def add(a, b):
    result = 0
    for i in range(a, b + 1):
        result += (numb3+i)
    print(result)

def minus(a,b):
    result = 0
    for i in range(int(a), int(b) + 1):
        result += (i-numb3)
    print(result)

def times(a,b):
    result = 0
    for i in range(int(a), int(b) + 1):
        result += (i*numb3)
    print(result)

def modula(a,b):
    result = 0
    for i in range(int(a), int(b) + 1):
        result += (i%numb3)
    print(result)

def div(a,b):
    result = 0
    for i in range(int(a), int(b) + 1):
        result += (i/numb3)
    print(result)
        
SumCalc(numb1, numb2)