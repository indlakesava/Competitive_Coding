"""
Method 1
2 pointer approach
if you can notice this is nothing but partition approach where the pivot is not from the array but instead it's 0
Time Complexity = O(n)
"""
def move_negatives_2ptr(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i]<0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums

lst = [1, -3, 6, 8, -5, 0, -10]
print(lst)
print(move_negatives_2ptr(lst))
