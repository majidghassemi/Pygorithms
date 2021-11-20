def bubble_sort(the_list):
    for i in range(1, len(the_list)):
        temp = the_list[i]
        j = i - 1
        while temp < the_list[j] and j >= 0:
            the_list[j + 1] = the_list[j]
            the_list[j] = temp
            j -= 1
    return the_list
