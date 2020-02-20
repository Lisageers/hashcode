from random_alg import random_alg

def hillclimb(data):
    dict_write = {'score': 0}

    for i in range(100):
        dict_temp = random_alg(data)

        if dict_temp['score'] > dict_write['score']:
            dict_write = dict_temp

    with open('result.txt', 'w') as file:
        file.write(f"{dict_write['amount_libraries_setup']}\n")

        for library in dict_write['libraries_setup']:
            file.write(f"{library} {len(dict_write['sent_books'][library])}\n")

            for book in dict_write['sent_books'][library]:
                file.write(f'{str(book)} ')
            
            file.write('\n')
        
    print('highest:', dict_write['score'])