def main():

    List = [23, 12, 45, 21, 1]

    Inserted_list = insertion(List)
    print(Inserted_list)

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

if __name__ == "__main__":
    main()