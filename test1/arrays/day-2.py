def equalSumSubarray(arr):
    s = sum(arr)
    s = s // 2
    # Here the problem reduces to finding all subarrays with sum s


eqSum = [1, 2, 3, 4, 5, 5, 6]
equalSumSubarray(eqSum)


# Find all subarrays of given array
def findSubarray(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print("\n", end=" ")


findSubarr = [1, 2, 3, 4]


# findSubarray(findSubarr)

# Find sum in contiguous subarray
def getSum(arr, sum):
    i = j = 0
    lst = []
    temp = 0
    for i in range(len(arr)):
        if temp == sum:
            break
        if temp < sum:
            temp += arr[i]
            lst.append(arr[i])
        elif temp > sum:
            lst.remove(arr[j])
            temp -= arr[j]
            j = j + 1

    return lst


# print(getSum(eqSum,11)) # Not accurate answer, some edge cases are failing

def productArr(arr, prod):
    temp = arr[0]
    for i in range(0,len(arr)):
        temp = arr[i]
        for j in range(i+1, len(arr)):
            temp *= arr[j]
            # print('temp'+str(temp))
            if temp == prod:
                return True
    return False


pr = [-2, -1, 3, -4, 5]
# print(productArr(pr,-20)) # Notice the test cases, loop starting and ending positions are crucial
