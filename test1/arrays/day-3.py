# Hashmap based Checking pair with given sum

def checkPair(arr, sum):
    hashmap = {}
    for i in range(len(arr)):
        temp = sum - arr[i]
        if temp in hashmap:
            print("Yes")
            return
        hashmap[arr[i]] = 1
    print('No')
    return


A = [1, 4, 45, 6, 10, 8]
n = 17


checkPair(A,n)

# Sort elements by frequency
# Input : arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
# Output : arr[] = {8, 8, 8, 2, 2, 5, 5, 6}
#
# Input : arr[] = {2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8}
# Output : arr[] = {8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999}


def sortFrequency(arr):
    hashmap = collections.defaultdict(int)
    for i in range(len(arr)):
        hashmap[arr[i]] += 1
    arr.sort(key=lambda x: (-hashmap[x], x))
    print(arr)
    return


hm = [2, 5, 2, 8, 5, 6, 8, 8]
sortFrequency(hm)

