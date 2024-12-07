n = "ABSED"
m = "ABESED"


# D A B S E D
# C A B E D


#       A   B   S   E   D
#   A   1   0   0   0   0
#   B   0   2   0   0   0   
#   E   0   0   0   1   0
#   D   0   0   0   0   2

# if i == j : [i][j] =  1 + [i-1][j-1] : count + memorize

lcs = []
longest_len = 0

table = [[0] * (len(m) + 1) for _ in range(len(n) + 1)]

for i in range(1, len(n) + 1):
    for j in range(1, len(m) + 1):
        if n[i - 1] == m[j - 1]:
            table[i][j] = table[i - 1][j - 1] + 1
            if (new := table[i][j]) >= longest_len:
                longest_len = new
                lcs.append((new, i))

lcs = [i for (lengh, i) in lcs if lengh == longest_len]
result = []
for i in lcs:
    result.append(n[i - longest_len: i])
print(result)
