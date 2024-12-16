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


case = int(input())
for i in range(case):
    num = int(input())
    arr = list(map(int, input().split()))
    result = solver(num, arr)
    print(" ".join(map(str, result)))
