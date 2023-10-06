def arrayRotation(arr, k):
    temp = arr[:k]
    arr = arr[k:]
    for i in temp:
        arr.append(i)
    print(arr)
    return


a = [1, 2, 3, 4, 6, 5, 7, 1, 9]


arrayRotation(a, 3)


def countingSort(arr):
    hashmap = {}
    sorted = []
    for i in arr:
        hashmap[i] = hashmap.get(i, 0) + 1
    for k, v in hashmap.items():
        while v:
            sorted.append(k)
            v = v - 1
    print(sorted)
    return


countingSort(a)


# Subsequence
def subsequence_recursive(arr):
    if len(arr) == 0:
        return ['']
    temp = arr[0]
    subseq = []
    remArr = subsequence_recursive(arr[1:])
    for i in remArr:
        subseq.append(i)
        subseq.append(str(temp) + i)
    return subseq


input_string = 'India'
seq = subsequence_recursive(input_string)


# print(seq)


def get_all_subsequences(string):
    subsequences = ['']

    for char in string:
        current_subsequences = []

        for subsequence in subsequences:
            current_subsequences.append(subsequence)
            current_subsequences.append(subsequence + char)

        subsequences = current_subsequences

    return subsequences


# Test the function
input_string = 'India'


# subsequences = get_all_subsequences(input_string)
# print(subsequences)

def reverse(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    print(arr)
    return


# reverse(a)

c = [6, 1, 2, 8, 3, 4, 7, 10, 5]


def getMissingNo(b):
    n = len(b) + 1
    _sum = (n * (n + 1)) // 2
    _bsum = sum(b)
    print(_sum - _bsum)
    return


# getMissingNo(c)

def binarySearch(arr, target):
    l = 0
    n = len(arr)
    while l < n:
        m = (l + n) // 2
        if arr[m] == target:
            print('Target found at index: ' + str(m))
            return
        elif arr[m] < target:
            l = m + 1
        else:
            n = m - 1
    print("No Target found")
    return


a = [1, 2, 3, 4, 6, 5, 7, 1, 9]
binarySearch(a, 16)
