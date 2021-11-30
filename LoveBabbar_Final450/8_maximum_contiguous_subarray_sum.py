#Time Complexity = O(n)

def maxSubArraySum(arr):
        global_max = arr[0]
        local_max = arr[0]

        for i in range(1, len(arr)):
            local_max = max(arr[i], local_max+arr[i])
            global_max = max(local_max, global_max)
        return global_max

lst = [1,2,3,-2,5]
print(lst)
print(maxSubArraySum(lst))