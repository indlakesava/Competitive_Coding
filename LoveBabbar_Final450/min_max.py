#Time Complexity = O(n)

def Min_Max(nums):
    min_ele = nums[0]
    max_ele = nums[0]

    for i in nums:
        if i<min_ele:
            min_ele = i
        if i>max_ele:
            max_ele = i

    return (min_ele, max_ele)

lst = [2,5,3,6,2,1,4]
a,b = Min_Max(lst)
print('Minimum element:', a)
print('Maximum element:', b)