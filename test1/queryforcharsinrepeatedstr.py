# https://www.geeksforgeeks.org/queries-for-characters-in-a-repeated-string/
def query(st, i, j):
    while len(st) < j+1:
        st += str(st)
    if st[i] == st[j]:
        print("Yes")
    else:
        print("No")
