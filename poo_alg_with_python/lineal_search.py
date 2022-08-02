import random
import time

counter = 0

def lineal_search(list, goal):
    global counter
    match = False

    for element in list:  # O(n)
        counter += 1

        if element == goal:
            match = True
            break

    return match


if __name__ == '__main__':

    list_size = int(input('Please specify the list size: '))
    goal = int(input('Number to find: '))

    list = [random.randint(0, 100) for i in range(list_size)]

    start = time.time()
    found = lineal_search(list, goal)
    end = time.time()
    
    print(list)
    print(f'The element {goal} {"IS" if found else "IS NOT"} in the list')
    print(f'The number of iterations is: {counter}')
    print(f'Time used to find the target: {end - start} s')