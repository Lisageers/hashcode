import csv

def load(filename):
    data_dict = {}

    with open(filename) as file:
        data = list(csv.reader(file, delimiter=" "))
        lib_counter = 0

        for i, line in enumerate(data):
            if i == 0:
                data_dict['book_amount'] = line[0]
                data_dict['lib_amount'] = line[1]
                data_dict['days'] = line[2]
            elif i == 1:
                data_dict['scores'] = line
            elif not i % 2:
                data_dict[str(lib_counter)] = {
                    'book_amount': line[0],
                    'process': line[1],
                    'shipping': line[2],
                }
            else:
                data_dict[str(lib_counter)]['books'] = line
                lib_counter += 1
    
    return data_dict
        