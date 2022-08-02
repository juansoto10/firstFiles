import random
import time


def insertion_sort(list):
    counter = 0

    for index in range(1, len(list)):
        current_value = list[index]
        current_pos = index

        while current_pos > 0 and list[current_pos - 1] > current_value:
            counter += 1
            list[current_pos] = list[current_pos - 1]
            current_pos -= 1

        counter += 1
        list[current_pos] = current_value

    return (list, counter)


if __name__ == '__main__':

    my_list = [7, 5, 3, 8, 1, 9, 2, 4, 6]
    print(my_list)

    start = time.time()
    sorted_list, counter = insertion_sort(my_list)
    end = time.time()
    
    print(sorted_list)
    print(f'The list was sorted in {end - start} s and {counter} iterations')


