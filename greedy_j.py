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
    books = {}

    for library in libraries_to_load:
        book_scores = []
        books[library] = []

        for book in data[library]['books']:
            book_scores.append(scores[book])

        for i in range(len(book_scores)):
            max_value = max(book_scores)
            books[library].append(data[library]['books'].pop(book_scores.index(max_value)))
            del book_scores[book_scores.index(max_value)]

    for day in range(days):
        if day >= day_setup and len(libraries_to_load):
            if lib_load:
                libraries_setup.add(lib_load)

            lib_load = libraries_to_load.pop(0)
            day_setup = day + data[lib_load]['process']

        for library in libraries_setup:
            books_to_send = set()

            try:
                for i in range(data[library]['shipping']):
                    books_to_send.add(books[library].pop(0))
            except IndexError:
                pass

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

    with open('result.txt', 'w') as file:
        file.write(f"{dict_write['amount_libraries_setup']}\n")

        for library in dict_write['libraries_setup']:
            file.write(f"{library} {len(dict_write['sent_books'][library])}\n")

            for book in dict_write['sent_books'][library]:
                file.write(f'{str(book)} ')
            
            file.write('\n')

    print(dict_write['score'])
    return sum(score)