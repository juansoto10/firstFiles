def run():
    
    # Using for loops:

    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # print(squares)

    # We can also do this in one line using list_comprehensions:

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    print(squares)

    # Creating a list with multiples of four that are also multiples of 6 and 9 (up to 5 digits) using list comprehensions:

    multiples = [i for i in range(1, 100000) if i % 36 == 0]

    print(multiples)


if __name__ == '__main__':
    run()