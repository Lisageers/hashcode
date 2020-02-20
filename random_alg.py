import random as rnd
import copy

def random_alg(data):
    days = data['days']
    libraries_to_load = list(data.keys())[4:]
    libraries_setup = set()
    day_setup = 0
    lib_load = None
    score = []
    scores = data['scores']
    sent_books = {}
    books_sent = set()
    
    for day in range(days):
        if day >= day_setup and len(libraries_to_load):
            if lib_load:
                libraries_setup.add(lib_load)

            lib_load = rnd.choice(libraries_to_load)
            del libraries_to_load[libraries_to_load.index(lib_load)]
            day_setup = day + data[lib_load]['process']

        for library in libraries_setup:
            try:
                books_to_send = set(rnd.sample(data[library]['books'], data[library]['shipping']))
            except ValueError:
                books_to_send = set(data[library]['books'])
            set(data[library]['books']) - books_to_send

            if library in sent_books:
                for book in books_to_send:
                    sent_books[library].add(book)
            else:
                sent_books[library] = books_to_send

            for book in books_to_send:
                books_sent.add(book)
    
    for book in books_sent:
        score.append(scores[book])

    dict_write = {
        'amount_libraries_setup': len(libraries_setup),
        'libraries_setup': libraries_setup,
        'sent_books': sent_books,
        'score': sum(score)
    }

    print(sum(score))
    return dict_write



