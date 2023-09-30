# Recursion is used. split the list into sublist with 1 element and remaining elements and then add 1 element at start of each recursion.
# Lets take ['a','b','c'] as example, take a first
# a,bc
# bc,a
# Then swap b with a
# b,ac
# ac,b

# Then swap c with a
# c,ba
# ba,c

# Then swap b with c (Note use double loop to swap elements)
# a,cb
# cb,a

def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]

        for p in permutation(remLst):
            l.append([m] + p)

    return l

data = list('123')
p = permutation(data)
print(p)

data = list('1234')
p = permutation(data)
print(p)

