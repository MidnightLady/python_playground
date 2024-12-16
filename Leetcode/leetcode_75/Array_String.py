import math


def gcd_string(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    gcd_len = math.gcd(len(str1), len(str2))
    return str1[:gcd_len]


a = "ABCABC"
b = "ABC"


# print(gcd_string(a, b))


def merge_string(str1, str2):
    result = ""
    i = 0
    for i in range(len(str1)):
        result += str1[i]
        if i < len(str2):
            result += str2[i]
    result += str2[i + 1:]
    return result


a = "ab"
b = "zxcd"


# print(merge_string(a, b))


def kidsWithCandies(candies, extraCandies):
    _max = max(candies)
    result = [True] * len(candies)
    for i, c in enumerate(candies):
        if c + extraCandies < _max:
            result[i] = False
    return result


a = [1, 2, 3, 4]


# kidsWithCandies(a, 2)


def canPlaceFlowers(flowerbed, n: int) -> bool:
    prev = 0
    for a, i in enumerate(flowerbed):
        if n == 0:
            if i == prev == 1:
                return False
            else:
                break
        if i == 0:
            _next = 0 if a == len(flowerbed) - 1 else flowerbed[a + 1]
            if prev == 0 and _next == 0:
                flowerbed[a] = 1
                n -= 1
        prev = flowerbed[a]
    return True if n == 0 else False


a = [0, 1, 0, 1, 0, 1, 0, 0]
b = 1


# print(canPlaceFlowers(a, b))

def reverseVowels_Array(s: str) -> str:
    vowels = []
    l = ['a', 'e', 'i', 'u', 'o']
    for i, v in enumerate(s):
        if v.lower() in l:
            vowels.append(v)
    if not vowels:
        return s
    result = list(s)
    for i in range(len(result)):
        if result[i].lower() in l:
            result[i] = vowels.pop()

    return "".join(result)


def reverseVowels_2Poiter(s: str) -> str:
    l = "aeiouAEIOU"
    right = len(s)
    s = list(s)
    for left in range(len(s)):
        if s[left] in l:
            while right > left:
                right -= 1
                if s[right] in l:
                    s[left], s[right] = s[right], s[left]
                    break
        if left >= right:
            break
    return "".join(s)


str = "AceCreIm"


# print(reverseVowels_2Poiter(str))


def reverseWords(s: str) -> str:
    s = s.split(" ")[::-1].filter()
    s = [i for i in s if i]
    return " ".join(s)


str1 = "a b c d   e  "


# print(reverseWords(str1))


def findMaxAverage(nums, k) -> float:
    prev = sum(nums[0:k])
    max_sum = prev
    for i in range(1, len(nums) - k + 1):
        prev = prev + nums[i + k - 1] - nums[i - 1]
        max_sum = max(prev, max_sum)
    return max_sum / k


a = [4, 2, 1, 3, 3]
k = 2


# print(findMaxAverage(a, k))

def maxVowels(s, k):
    current = 0
    l = 'aeiou'
    sub = s[0:k]
    for i in sub:
        if i in l:
            current += 1
    max_vowel = current
    for i in range(1, len(s) - k + 1):
        if s[i - 1] in l:
            current -= 1
        if s[i + k - 1] in l:
            current += 1
        max_vowel = current if current > max_vowel else max_vowel

    return max_vowel


str = "abciiidef"
k = 3
print(maxVowels(str, k))


def pivotIndex(nums) -> int:
    left = 0
    right = sum(nums)
    for i in range(len(nums)):
        left += nums[i - 1] if i > 0 else 0
        right -= nums[i]
        if left == right:
            return i
    return -1



