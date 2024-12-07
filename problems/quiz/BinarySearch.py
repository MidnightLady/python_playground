def search_left(sorted_list, x):
    low = 0
    high = len(sorted_list)

    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] < x:
            low = mid + 1
        else:
            high = mid

    return low


def search_right(sorted_list, x):
    low = 0
    high = len(sorted_list)
    
    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] <= x:
            low = mid + 1
        else:
            high = mid

    return low


unsort_a = [4, 6, 2, 7, 3, 4, 8, 1, 9, 5]
sort_a = sorted(unsort_a)
print(sort_a)
print(search_left(sort_a, 4))
print(search_right(sort_a, 4))
