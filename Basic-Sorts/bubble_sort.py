def bubble_sort(the_list):
    for i in range(len(the_list) - 1, 0, -1):
        for j in range(i):
            if the_list[j] > the_list[j + 1]:
                temp = the_list[j]
                the_list[j] = the_list[j + 1]
                the_list[j + 1] = temp

    return the_list
