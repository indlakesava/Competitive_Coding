#Time Complexity = O(n)

def reverse(nums):
    i = 0
    j = len(nums)-1

    while(i<j):
        nums[i],nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    return nums

lst = [2,5,3,6,2,1,4]
print(lst)
print(reverse(lst))