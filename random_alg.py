import random as rnd

def random_alg(data):
    days = data['days']
    
    libraries = list(data.keys())[4:]
    first_lib = rnd.choice(libraries)
    print(first_lib)