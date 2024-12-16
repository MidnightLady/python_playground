"""
Problem: https://codeforces.com/contest/2046/problem/A

approach: find the pivot, then push all remaining elements to left or right pivot
          maximum cost when row1[i] > row2[i] will be in left and row1[i] < row2[i] will be in right
          => symply max(row1[i], row2[i]) for every element cause we dont need to return array has maximum cost.
          time complexity: O(n)
          space complexity: O(1)
"""


def solver(n, row1, row2):
    if n == 1:
        return row1[0] + row2[0]
    # cost as pivot  and  cost it should gain if not being a pivot
    pivot = (row1[0] + row2[0], max(row1[0], row2[0]), 0)
    for i in range(1, n):
        p = (row1[i] + row2[i], max(row1[i], row2[i]), i)
        if p[0] + pivot[1] > pivot[0] + p[1]:
            pivot = p

    total = pivot[0]
    for i in range(n):
        if pivot[2] != i:
            total += max(row1[i], row2[i])
    return total



