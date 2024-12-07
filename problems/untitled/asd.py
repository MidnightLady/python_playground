import timeit

g = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
c = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]
'''
    -4 -1  0 -5 -2 -3 -4 -6  -3  0
    -4  3  1 -5  3  -1 -1 -2 3   3
prev > 0
start: gas > cost : left = gas - cost
next:  left + gas > cost: update left += gas - cost 

'''


def dfs(graph, start, visited):
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


from collections import deque


def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            for neighbor in graph[vertex]:
                queue.append(neighbor)
    return visited


# build graph

graph = {
    1: [0, 2, 4],
    0: [3],
    3: [1, 5],
    2: [4],
    4: [5]
}


def course_schedule(numCourses, prerequisites):
    from collections import defaultdict
    graph = defaultdict(list)
    for c, req in prerequisites:
        graph[req].append(c)
    visited = [0] * numCourses

    def dfs(course):
        if visited[course] == -1:
            return False
        if visited[course] == 1:
            return True
        visited[course] = -1
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
        visited[course] = 1
        return True

    for i in range(numCourses):
        if visited[i] == 0:
            if not dfs(i):
                return False
    return True


#
#
# numCourses = 6
# prerequisites = [[1, 0], [3, 2], [1, 3], [5, 4]]
# print(canFinish(numCourses, prerequisites))


'''  ()()() ((())) (())() ()(())
 - start with (
 - ( < n and ) < n
 - if ( == ) : ínsert (
'''
#

#
#
combs = []


def generate(n, comb='', left=0, right=0):
    if len(comb) == 2 * n:
        combs.append(comb)
        return
    if left < n:
        generate(n, comb + '(', left + 1, right)
    if left > right:
        generate(n, comb + ')', left, right + 1)


#
#
generate(3)
print(combs)

#
#
#         3! -> 2x3       6
#         4! -> 2x3x4      24
#         5!  2x3x4x5
# 1   24
# 2   24
# 3   24
# 4   24
# 5   24
#                                    n=4  k = 5
#
# 123
# 132
#                     lengh = n
#                     first :  k // (n-1)!    unuse = [1,2,3...n].remove(first)
#                     next ?    k // (n-2)!
#
#
#
# 1234
# 1243
#
# 1324
# 1342
#
# 1423    x
# 1432
# 2134
# 2 x6
# 3 x6
# 4 x 6
#
n = 141
k = 2234


def kth_permutation(n, k):
    numbers = [i + 1 for i in range(n)]
    import math
    num = ''
    while len(numbers) > 0:
        n -= 1
        add = (k - 1) // math.factorial(n)
        num += str(numbers.pop(add % len(numbers)))
    return int(num)


print(kth_permutation(n, k))

# A B C D E F G
# A D E
'''
        A   F   D   E   A   E   D   E
    A   0   1   1   1   1   1   1   1
    D   0   1   2   2   2   2   1   0
    E   1   1   2   2   2   3   3   1
'''

a = 'AFDEAEDE'
b = 'ADEE'

'''
COUNTER b
run R until = COUNTER b
get min and try to minimize window
'''


def shortest_string(a, b):
    from collections import Counter
    count_b = Counter(b)
    count_a = {char: 0 for char in count_b.keys()}
    left = 0
    res = len(a), None, None
    check = 0
    for right in range(len(a)):
        if (char := a[right]) in count_a:
            count_a[char] += 1
            if count_a[char] == count_b[char]:
                check += 1
        # trying to smaller window if enough count
        while left <= right and check == len(count_b):
            if (length := right - left + 1) < res[0]:
                res = length, left, right
            if (char := a[left]) in count_a:
                count_a[char] -= 1
                if count_a[char] < count_b[char]:
                    check -= 1
            left += 1
    return "" if res[1] is None else a[res[1]:res[2] + 1]


print("shortest_string", shortest_string(a, b))

'''
    slide [0:5]: sum 0-5 -> [1:6] sum[0:5] - [0] + [6]
    sum: min in rec[0:5] -> k * min
    every side: add [next] to rec -> re-calc min [i:k+i]  -> update min rec

         |
      |  ||
      |||||
     |||||||
'''



from collections import deque


def max_area_with_k_length(heights, k):
    n = len(heights)
    deq = deque()
    max_area = 0

    for i in range(n):
        while deq and heights[deq[-1]] >= heights[i]:
            deq.pop()
        deq.append(i)

        if deq[0] < i - k + 1:
            deq.popleft()

        if i >= k - 1:
            max_area = max(max_area, heights[deq[0]] * k)

    return max_area

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
k = 3
print("Max Area with length", k, ":", max_area_with_k_length(heights, k))



from collections import Counter


def minimumPushes(word: str) -> int:
    count = Counter(word).values()
    count = sorted(count, reverse=True)
    push = 0
    print(count)
    for index, num in enumerate(count):
        push += num * ((index // 8) + 1)
        print(((index // 8) + 1))
    return push


a = "aabbccddeeffgghhiiiiii"


print(minimumPushes(a))