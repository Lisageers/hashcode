import random as rnd

def random_alg(data):
    days = data['days']
    libraries_to_load = list(data.keys())[4:]
    libraries_setup = set()
    day_setup = 0
    lib_load = None
    score = set()
    scores = data['scores']
    
    for day in range(days):
        if day >= day_setup and len(libraries_to_load):
            if lib_load:
                libraries_setup.add(lib_load)

            lib_load = rnd.choice(libraries_to_load)
            del libraries_to_load[libraries_to_load.index(lib_load)]
            day_setup = day + data[lib_load]['process']

        for library in libraries_setup:
            books_to_send = set(rnd.sample(data[library]['books'], data[library]['shipping']))
            data[library]['books'] - books_to_send

            for book in books_to_send:
                score.add(scores[book])

    print(sum(score))

