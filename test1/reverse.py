
# Reverse words in given string
def reverseWords(str):
    st = str.split(" ")
    for i in st:
        pass
    st = st[::-1]
    st = " ".join(st)
    print(st)

s = "geeks quiz practice code"
reverseWords(s)

