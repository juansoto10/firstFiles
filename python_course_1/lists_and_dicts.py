def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Juan', 'lastname': 'Soto'}

    super_list = [
        {'firstname': 'Juan', 'lastname': 'Soto'},
        {'firstname': 'Miguel', 'lastname': 'Velasco'},
        {'firstname': 'Luis', 'lastname': 'Soto'},
        {'firstname': 'Claudia', 'lastname': 'Velasco'},
        {'firstname': 'Zuri', 'lastname': 'Soto'},
    ]

    super_dict = {
        'natural_numbers': [1, 2, 3, 4, 5],
        'integer_numbers': [-2, -1, 0, 1, 2],
        'floating_numbers': [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    for llavecita in super_dict.keys():
        print(llavecita)

    for rumba in super_list:
        print(rumba)


if __name__ == '__main__':
    run()