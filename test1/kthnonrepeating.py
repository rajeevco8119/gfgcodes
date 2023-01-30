# https://www.geeksforgeeks.org/kth-non-repeating-character/
def kthnonrepeating(arr, key):
    freq = {}
    l = key
    for i in arr:
        if i in freq.keys():
            freq[i] += 1
        else:
            freq[i] = 1
    for k, v in freq.items():
        if v == 1 and l == 1:
            return k
        elif v == 1:
            l -= 1
        else:
            continue
    return "Less than k non-repeating chars"
