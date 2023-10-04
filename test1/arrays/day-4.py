
# K most occuring numbers

def KMostOccuring(arr, k):
    hashmap = {}
    for i in range(len(arr)):
        if arr[i] in hashmap.keys():
            hashmap[arr[i]] += 1
        else:
            hashmap[arr[i]] = 1
    a = [0] * (len(hashmap))
    j = 0
    for i in hashmap:
        a[j] = [i, hashmap[i]]
        j += 1
    print(a)
    a = sorted(a, key=lambda x: x[0], reverse=True)
    a = sorted(a, key=lambda x: x[1], reverse=True)
    for i in range(k):
        print(a[i][0])


ar = [3, 1, 4, 4, 5, 2, 6, 1]
# KMostOccuring(ar,2)


import heapq


def print_N_mostFrequentNumber(arr, N, K):
    mp = dict()

    for i in range(0, N):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        else:
            mp[arr[i]] += 1

    heap = [(v, k) for k, v in mp.items()]
    # print(heap)
    largest = heapq.nlargest(K, heap)
    for i in range(K):
        print(largest[i][1], end=" ")


# print_N_mostFrequentNumber(ar, len(ar), 2)

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m - 1, n), lcs(X, Y, m, n - 1))


S1 = "AGGTAB"
S2 = "GXTXAYB"


# print("Length of LCS is", lcs(S1, S2, len(S1), len(S2)))


def kth_smallest(arr, k):
    max_element = max(arr)

    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1


arr9 = [12, 3, 5, 7, 19]
k2 = 2


# kth_smallest(arr9,k2)

# Construct an array from its pair-sum array

def pairSum(arr):
    s = sum(arr)
    n = s // 3


def reverse(arr):
    if len(arr) == 0:
        return
    temp = arr[0]
    reverse(arr[1:])
    print(temp)


# reverse(arr9)

def removeChar(arr, char):
    c = []
    for i in arr:
        if i == char:
            continue
        c.append(i)
    d = "".join(c)
    print(d)


removeChar('geeksforgeeks', 'e')
