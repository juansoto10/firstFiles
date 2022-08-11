import random

def merge_sort(list):

    if len(list) > 1:

        middle = len(list) // 2
        left = list[:middle]
        # print(left)
        right = list[middle:]
        # print(right)
        print(left, '|' * 6, right)

        # Recursive call in each section:

        merge_sort(left)
        merge_sort(right)

        # Iterators for the 2 sub-lists:

        i = 0
        j = 0

        # Iterator for the main list:

        k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):

            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):

            list[k] = right[j]
            j += 1
            k += 1

        print(f'Left: {left}, Right: {right}')
        print(list)
        print('-' * 25)

    return list


if __name__ == '__main__':

    list_size = int(input('Please specify the list size: '))
    my_list = [random.randint(0, 100) for i in range (list_size)]
    print(my_list)
    print('-' * 15)

    sorted_list = merge_sort(my_list)
    print(sorted_list)

# Output example:

# Please specify the list size: 6
# [44, 82, 18, 25, 92, 57]
# ---------------
# [44, 82, 18] |||||| [25, 92, 57]
# [44] |||||| [82, 18]
# [82] |||||| [18]
# Left: [82], Right: [18]
# [18, 82]
# -------------------------
# Left: [44], Right: [18, 82]
# [18, 44, 82]
# -------------------------
# [25] |||||| [92, 57]
# [92] |||||| [57]
# Left: [92], Right: [57]
# [57, 92]
# -------------------------
# Left: [25], Right: [57, 92]
# [25, 57, 92]
# -------------------------
# Left: [18, 44, 82], Right: [25, 57, 92]
# [18, 25, 44, 57, 82, 92]
# -------------------------
# [18, 25, 44, 57, 82, 92]