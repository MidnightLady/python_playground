"""
    problem: https://codeforces.com/contest/2046/problem/B
    Approach: sort the array with every element should keep its index
              iterate the sorted array:
                  if index is less than current index, it means element need to push to right
                  else the element in right place, add to result and update current index
              => need get the smallest element, and update array everytime, so we should use heap
    time complexity: O(nlogn)
    space complexity: O(n)


"""
import heapq


def solver(n, arr):
    index_arr = []
    res = []
    for index, value in enumerate(arr):
        index_arr.append((value, index))
    heapq.heapify(index_arr)

    cur = 0
    while index_arr:
        value, index = heapq.heappop(index_arr)
        if index == n or index >= cur:
            cur = index
            res.append(value)
        else:
            heapq.heappush(index_arr, (value + 1, n))
    return res



