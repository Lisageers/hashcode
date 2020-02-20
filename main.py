from load import load
from greedy import greedy
from random import random
from sys import argv

if len(argv) < 3:
    print('typ an argument')
    exit()

algorithm = argv[2]
filename = argv[1]

data = load(filename)

if algorithm == 'rand':
    random(data)
elif algorithm == 'greedy':
    greedy(data)
