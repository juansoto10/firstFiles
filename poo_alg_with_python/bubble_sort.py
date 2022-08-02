import random
import time


def bubble_sort(list):
    n = len(list)

    for i in range(n):  # O(n) * O(n) == O(n**2)
        for j in range(0, n - i - 1):

            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list



if __name__ == '__main__':

    list_size = int(input('Please specify the list size: '))

    my_list = [random.randint(0, 100) for i in range(list_size)]
    print(my_list)

    start = time.time()
    sorted_list = bubble_sort(my_list)
    end = time.time()

    print(sorted_list)

    # print(f'The number of iterations is: {counter}')
    print(f'Time used: {end - start} s')