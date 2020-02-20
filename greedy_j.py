import random as rnd

def jordy(data):
    days = data['days']
    libraries_to_load = list(data.keys())[4:]
    libraries_to_load.sort()
    libraries_setup = set()
    day_setup = 0
    lib_load = None
    score = []
    scores = data['scores']
    sent_books = {}
    books_sent = set()

    for library in libraries_to_load:
        data[library]['books']
    
    for day in range(days):
        if day >= day_setup and len(libraries_to_load):
            if lib_load:
                libraries_setup.add(lib_load)

            lib_load = libraries_to_load.pop(0)
            day_setup = day + data[lib_load]['process']

        for library in libraries_setup:
            try:
                books_to_send = set(rnd.sample(data[library]['books'], data[library]['shipping']))
            except ValueError:
                books_to_send = set(data[library]['books'])
            data[library]['books'] - books_to_send

            if library in sent_books:
                for book in books_to_send:
                    sent_books[library].add(book)
            else:
                sent_books[library] = books_to_send

            for book in books_to_send:
                books_sent.add(book)

    with open('result.txt', 'w') as file:
        file.write(f'{len(libraries_setup)}\n')

        for library in libraries_setup:
            file.write(f'{library} {len(sent_books[library])}\n')

            for book in sent_books[library]:
                file.write(f'{str(book)} ')
            
            file.write('\n')
    
    for book in books_sent:
        score.append(scores[book])

    print(sum(score))
    return sum(score)