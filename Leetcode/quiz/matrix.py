import timeit


def generate_matrix(rows, cols):
    return [[col + row * cols + 1 for col in range(cols)] for row in range(rows)]


# output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
# complexity : O(m*n) space 0(m*n)
# performance: comparition, iteration => less comparition, less iteration => less time, better performance
# while : read state => append to result


matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]


def spiral_travesal(arr):
    result = []
    while arr:
        # left to right
        result += arr.pop(0)
        if arr:
            # top to bot
            for i in range(len(arr)):
                result.append(arr[i].pop())

        # right to left
        if arr:
            result += arr.pop()[::-1]

        # bot to top
        if arr:
            for i in range(len(arr)):
                result.append(arr[-i - 1].pop(0))
    return result


print(spiral_travesal(matrix))
