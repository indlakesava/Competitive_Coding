#Time Complexity = O(n)

"""
Method 1
2 Pointer method where
"""
def sort(nums):
    low=0
    mid=0
    n=len(nums)
    high=n-1
    while(mid<=high):
        if(nums[mid]==0):
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif(nums[mid]==1):
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums

lst = [2,0,2,1,1,0]
print(sort(lst))


"""
Method 2
Count number of zeros, ones and twos and then replace the array with respective number of corresponding elements
"""
def sort012(arr):
    zeros = 0
    ones = 1
    twos = 2
    for i in arr:
    	if i==0:
    		zeros += 1
    	elif i==1:
    		ones += 1
    	elif twos==1:
    		twos += 1

    for i in range(zeros):
    	arr[i] = 0

    for i in range(zeros, zeros+ones-1):
    	arr[i] = 1

    for i in range(zeros+ones-1, len(arr)):
        arr[i] = 2

    return arr

lst = [2,0,2,1,1,0]
print(sort012(lst))