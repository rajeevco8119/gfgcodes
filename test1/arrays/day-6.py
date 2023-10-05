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

