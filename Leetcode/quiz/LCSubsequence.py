
'''
    todo: many route can be made: GA GB -> C
    expect: GAC, GBC
    current: GBC only, need handle sale tail: C
'''
n = "ABCBDABEF"
m = "BDCAB"

# list c[n][m]
dp = [[0] * (len(m) + 1) for _ in range(len(n) + 1)]

#       A   B   C   B   D   A   B
#   B   0   1   1   1   1   1   1
#   D   0   1   1   1   2
#   C   0   1   2   2   2
#   A   1   1   2   2   2
#   B   1   2   2   3   3

# if i == j : [i][j] = [i-1][j-1] + 1
# else: tracking [i][j] = max([i-1][j],[i][j-1])because subsequence is non-consecutive substring => need to tracking even not equal
#  result = c[n][m]
lcs: [()] = []
for i in range(1, len(n) + 1):
    for j in range(1, len(m) + 1):
        if n[i - 1] == m[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            lcs.append((dp[i][j], i, j))
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp)
# filter largest
lcs = [i for i in lcs if i[0] == dp[len(n)][len(m)]]
print(lcs)

commons = []




def retracking(_iter):
    count, i, j = _iter
    common = []
    while count > 0:
        if n[i - 1] == m[j - 1]:
            common.append(n[i - 1])
            count -= 1
            i, j = i - 1, j - 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return common

# find all common string
def backtrack(i, j):
    if i == 0 or j == 0:
        return {""}

    if n[i - 1] == m[j - 1]:
        # if match, add to result
        return {s + n[i - 1] for s in backtrack(i - 1, j - 1)}
    else:
        # if not match, backtrack to find all possible
        lcs_set = set()
        if dp[i - 1][j] == dp[i][j]:
            lcs_set |= backtrack(i - 1, j)
        if dp[i][j - 1] == dp[i][j]:
            lcs_set |= backtrack(i, j - 1)
        return lcs_set


all_set = backtrack(len(n), len(m))
print(all_set)

for c, ni, mj in lcs:
    common = retracking((c, ni, mj))
    commons.append(''.join(reversed(common)))

print(commons)
