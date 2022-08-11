from array import array
import random


def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f'Pivot: {pivot}\n Left: {left}\n Middle: {middle}\n Right: {right}')

    return merge_sort(left) + middle + merge_sort(right)


if __name__ == '__main__':

    arr_size = int(input('Please specify the list size: '))
    my_arr = [random.randint(1, 100) for i in range(arr_size)]
    print(my_arr)

    sorted_arr = merge_sort(my_arr)
    print(sorted_arr)