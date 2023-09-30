# Remove duplicates
def removeDuplicates(nums):
    c = []
    for i in nums:
        if i not in c:
            c.append(i)
        else:
            continue
    print(c)


a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


# removeDuplicates(a) o/p: [0, 1, 2, 3, 4]


# Subarray with a given sum
# simple apprach

def subarray_sum(arr, sum_, n):
    new_sum = 0
    for i in range(n):
        new_sum = arr[i]
        for j in range(i + 1, n):
            new_sum += arr[j]
            print(str(new_sum) + " i=" + str(i) + " : j=" + str(j))
            if new_sum == sum_:
                return True
    return False


arr = [15, 2, 4, 8, 9, 5, 10, 23]
sum_ = 23


print(subarray_sum(arr,sum_,len(arr)))

# Maximum Subarrays
nums = [-2, -3, 4, -1, -2, 1, 5, -3]


def max_subarray(arr):
    sum = 0
    max_sum = 0
    for i in range(len(arr)):
        max_sum = max(max_sum, sum)
        sum += arr[i]

        if sum < 0:
            sum = 0

    return max_sum


print(max_subarray(nums))


# all possible pairs in list
def all_pairs(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print("(" + str(i) + "," + str(j) + ")")
    return


b = [0, 1, 4, 3, 2]
all_pairs(b)

def swap(a, b):
    return b, a

print(swap(1, 2))

# Reverse words in string
def reverseWords(str):
    lst = str.split(" ")
    j = list()
    for i in lst:
        j.append(i[::-1])

    return " ".join(j)


c = "i love programming very much"
print(reverseWords(c))

