# Collatz Conjecture
'''
The Collatz conjecture (also known as the Ulam Conjecture or the Syracuse problem) is an unsolved mathematical
problem, which is very easy to formulate:

1. Take any natural number
2. if it's even, half it, otherwise triple it and add one
3. Repeat step 2, until you reach 4,2,1 sequence
4. You will ALWAYS reach 1, eventually

Example:
x = 17

17*3 + 1 = 52
52/2 = 26
26/2 = 13
13 *3 +1 = 40
40/2 = 20
20/2 = 10
10/2 = 5
5*3 + 1 = 16
16/2 = 8
8/2 = 4
4/2 = 2
2/2 = 1
...

The last sequence: 4,2,1 is an infinitely repeating loop. The formulated conjecture is that for any
x the sequence will always reach 4,2,1 ultimately.
'''
input = input() # int, natural number
count = 0
number = int(input)
while number > 1:
    count +=1
    if number%2 == 0:
        number /= 2
        number = int(number)
    else:
        number = number*3+1

    print(str(count) + '.\t' + str(number))
print('iteration = ' + str(count) + ' times.')

#Done