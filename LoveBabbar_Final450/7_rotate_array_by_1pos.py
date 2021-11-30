#Time Complexity = O(n)

def rotate(nums):
    return nums[1:]+nums[:1]

lst = [2,5,3,6,2,1,4]
print(lst)
print(rotate(lst))