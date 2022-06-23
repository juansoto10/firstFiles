from functools import reduce


def run():
    
    #list comprehension:

    # Printing the odd nummbers in my_list
    my_list = [1, 2, 5, 7, 14, 16, 19, 21, 23, 26, 29, 30, 33]

    odd = [i for i in my_list if i % 2 != 0]

    print(odd)

    # --> [1, 5, 7, 19, 21, 23, 29, 33]


    # Filter:

    # Printing the odd nummbers in my_list
    weird = list(filter(lambda x: x % 2 != 0, my_list))

    # --> [1, 5, 7, 19, 21, 23, 29, 33]

    print(weird)


    # Map:

    # Obtaining the square of each number in my_list
    squares = list(map(lambda x: x**2, my_list))

    print(squares)

    # --> [1, 4, 25, 49, 196, 256, 361, 441, 529, 676, 841, 900, 1089]


    # Reduce:

    # Multiplying the elements of my_list_2

    # For loop
    my_list_2 = [2, 2, 2, 2, 2]
    all_multiplied = 1

    for i in my_list_2:
        all_multiplied = all_multiplied * i

    print(all_multiplied)

    # --> 32

    # Using reduce

    all_multiplied_2 = reduce(lambda a, b: a * b, my_list_2)

    print(all_multiplied_2)

    # --> 32


if __name__ == '__main__':
    run()