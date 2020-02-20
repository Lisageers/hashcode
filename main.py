from load import load
from greedy import greedy
from greedy_j import jordy
from random_alg import random_alg
from hillclimb import hillclimb
from sys import argv

if len(argv) < 3:
    print('typ an argument')
    exit()

algorithm = argv[2]
filename = argv[1]

data = load(filename)

if algorithm == 'rand':
    random_alg(data)
elif algorithm == 'greedy':
    greedy(data)
elif algorithm == 'hill':
    hillclimb(data)
elif algorithm == 'jor':
    jordy(data)
