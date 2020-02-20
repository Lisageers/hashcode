from load import load
from greedy import greedy
from random import random
from sys import argv

if len(argv) < 2:
    print('typ an argument')
    exit()

algorithm = argv[1]
filename = input("enter filename: ")

data = load(filename)

if algorithm == 'rand':
    random(data)
elif algorithm == 'greedy':
    greedy(data)
