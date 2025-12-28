import random

def throw(x):
    i = 1
    array = []
    while i <= x:
        kubik = random.randint(1, 6)
        array.append(kubik)
        i+=1
    return array

print(throw(5))

def check_throw(arr):
    for i in range()