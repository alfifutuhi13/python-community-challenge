'''
\
Password validator is a program that validates passwords to match specific rules.

A valid passowrd is the one that conforms to the following rules:
- Minimum uppercase is 1;
- Minimum length is 5;
- Maximum length is 10
- Should contain at least one number;
- Should contain at least one special character (such as &, +, @, $,#, %, etc.);
- Should not contain spaces/

Examples:
Input: "Sololearn"
Output: false

Input: "John Doe"
Output: false

Input: "$ololearn7"
Output: true
'''

#String Uppercase
uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lu = len(uppercase)
count_1 = 0

#String number
number = '1234567890'
ln=len(number)
count_2 = 0

#String special character
specialchar = '!@#$%^&*()_+-'
ls = len(specialchar)
count_3 = 0

input =input()

for char in input:
    for i in range(0,lu):
        if char == uppercase[i]:
            count_1 += 1
    for i in range(0,ln):
        if char == number[i]:
            count_2 += 1
    for i in range(0,ls):
        if char == specialchar[i]:
            count_3 += 1


if len(input)<5 or len(input)>10 or count_1 < 1 or count_2 < 1 or count_3 <1 or char == ' ':
    print('false')
else:
    print('true')

#Output is as expected!