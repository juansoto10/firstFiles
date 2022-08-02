import random
import time

counter = 0

def binary_search(list, start, end, target):
    
    print(f'Looking for {target} among the elements {list[start]} and {list[end - 1]}')

    global counter

    if start > end:
        return False

    middle = (start + end) // 2  # NOTA: '//' Significa 'división de enteros' (No importan los decimales)

    if list[middle] == target:
        counter += 1
        return True
    elif list[middle] < target:
        counter += 1
        return binary_search(list, middle + 1, end, target)
    else:
        counter += 1
        return binary_search(list, start, middle - 1, target)


if __name__ == '__main__':

    list_size = int(input('Please specify the list size: '))
    goal = int(input('Number to find: '))

    my_list = sorted([random.randint(0, 100) for i in range(list_size)])

    start = time.time()
    found = binary_search(my_list, 0, len(my_list), goal)
    end = time.time()

    print(my_list)
    print(f'The element {goal} {"IS" if found else "IS NOT"} in the list')
    print(f'The number of iterations is: {counter}')
    print(f'Time used to find the target: {end - start} s')