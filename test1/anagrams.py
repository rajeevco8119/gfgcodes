# https://www.geeksforgeeks.org/count-total-anagram-substrings/
def anagramcount(str):
    n = len(str)
    substrings = []
    count = 0
    for i in range(len(str)):
        temp = ""
        for j in range(i,n):
            temp += str[j]
            substrings.append(temp)
    for k in substrings:
        if k[::-1] in substrings and len(k)<len(str):
            count += 1
    print(count//2)

st2 = "xyyx"
anagramcount(st2)

