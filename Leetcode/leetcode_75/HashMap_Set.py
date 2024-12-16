def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return [list(set1 - set2), list(set2 - set1)]


nums1 = [1, 2, 3]
nums2 = [2, 4, 6, 2]
# print(findDifference(nums1, nums2))

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

intersection = list(set(arr1) & set(arr2))  # [3, 4]

difference = list(set(arr1) ^ set(arr2))  # [1, 2, 5, 6]

merged = list(set(arr1) | set(arr2))  # [1, 2, 3, 4, 5, 6]

only_in_arr1 = list(set(arr1) - set(arr2))

only_in_arr2 = list(set(arr2) - set(arr1))

from collections import Counter


def uniqueOccurrences(arr) -> bool:
    count = Counter(arr).values()
    count_unique = Counter(count).values()
    return True if set(count_unique) == {1} else False

import heapq
# arr = [1, 2, 2, 1, 1, 3]
# print(uniqueOccurrences(arr))
def findFailedPods(logs):
    server_list = []
    result = []
    for (_type, k) in logs:
        if _type == 1:
            heapq.heappush(server_list, k)
        if _type == 2:
            server_list = [i + k for i in server_list]
        if _type == 3:
            if server_list:
                result.append(heapq.heappop(server_list))
    return result