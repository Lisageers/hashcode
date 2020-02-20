from random_alg import random_alg

def hillclimb(data):
    total_score = 0

    for i in range(100):
        score = random_alg(data)

        if score > total_score:
            total_score = score
        
    print('highest:', total_score)