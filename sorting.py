def main():

    List = [23, 12, 45, 21, 1, 2, 39]

    Inserted_list = insertion(List)
    print(Inserted_list)

    Selected_list = selection(List)
    print(Selected_list)

    Merged_list = mergesort(List)
    print(Merged_list)

    Bubble_list = bubble_sort(List)
    print(Bubble_list)


def insertion(List):

    list = List

    i = 1

    while i < len(list):

        number = list[i]
        j = i - 1

        while j >= 0 and list[j] > number:

            list[j + 1] = list[j]
            j-=1

        list[j + 1] = number
        i = i + 1

    return list


def selection(List):

    list = List

    i = 0

    while i < len(list) - 1:

        minIndex = i
        j = i + 1

        while j < len(list):

            if list[j] < list[minIndex]:

                minIndex = j

            j += 1

        if minIndex != i:

            swap = list[i]
            list[i] = list[minIndex]
            list[minIndex] = swap

        i += 1
    return list


def mergesort(List):

    list = List

    if len(list) == 1:

        return list

    left = list[:len(list)//2]
    right = list[len(list)//2:]



    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


def merge(left_list, right_list):

    new_list = []

    while len(left_list) > 0 and len(right_list) > 0:

        if left_list[0] > right_list[0]:

            new_list.append(right_list[0])
            right_list = right_list[1:]

        else:

            new_list.append((left_list[0]))
            left_list = left_list[1: ]

    while len(left_list) > 0:

        new_list.append(left_list[0])
        left_list = left_list[1:]

    while len(right_list) > 0:

        new_list.append(right_list[0])
        right_list = right_list[1:]

    return new_list


def bubble_sort(List):

    list = List
    n = len(list)

    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

if __name__ == "__main__":
    main()