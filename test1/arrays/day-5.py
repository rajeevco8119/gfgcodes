def palindrome(arr):
    return arr == arr[::-1]

def removeSingleChars(arr):
    c = []
    for i in arr:
        if len(i) == 1:
            continue
        c.append(i)
    c = "".join(c)
    return c

# a = palindrome('rajar')

def allPalindromeSubstrings(arr,n):
    c = []
    for i in range(n):
        for len in range(i + 1, n+ 1):
            c.append(arr[i: len])
    # removeSingleChars(c)
    for i in c:
        if palindrome(i):
            print(i)
    return

# allPalindromeSubstrings('rajar',len('rajar'))

b = ['a','ab']
# removeSingleChars(b)

# I/P - aaaaabbbbcccdde , O/P a5b4c3d2e1

def compressedString(arr):
    hashmap = {}
    st = ''
    for i in arr:
        hashmap[i] = hashmap.get(i,0)+1
    for k,v in hashmap.items():
        st += str(k)+str(v)
    print(st)
compressedString('aaaaabbbbcccdde')
