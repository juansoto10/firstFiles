def run():
    
    # Using for loops:

    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    # print(my_dict)


    # Using dict. comprehensions:

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print(my_dict)

    # Creating a dict: keys --> The first 1000 natural numbers; values --> The square roots of the keys

    my_singular_dict = {i: i**0.5 for i in range(1, 1001)}

    print(my_singular_dict)


if __name__ == '__main__':
    run()