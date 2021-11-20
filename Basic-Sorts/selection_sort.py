def selection_sort(the_list):
    for i in range(len(the_list) - 1):
        min_index = i
        for j in range(i + 1, len(the_list)):
            if the_list[i] > the_list[j]:
                min_index = j
        if i != min_index:
            temp = the_list[i]
            the_list[i] = the_list[min_index]
            the_list[min_index] = temp
    return the_list
