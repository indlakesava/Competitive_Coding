"""
 *Method - 1
 * Have 2 for loop. j trails i. If arr[j] + j >= i then you calculate new jump and result.
 * https://www.youtube.com/watch?v=cETfFsSTGJI
 * Space complexity O(n) to maintain result and min jumps
 * Time complexity O(n^2)
"""
def minJump(arr):
    result = [0]*len(arr)
    jump = [max(arr)]*len(arr)
    jump[0] = 0

    for i in range(1, len(arr)):
        for j in range(0, i):
            if(arr[j] + j >= i):
                if(jump[i] > jump[j] + 1):
                    result[i] = j
                    jump[i] = jump[j] + 1
    return jump[len(jump)-1]

print(minJump([1, 4, 3, 2, 6, 7]))


"""
def minJumps(self, arr, n):
	    if n==1:
	        return 0
	        
        i = 0
        steps = 0
        while(i+arr[i] < n-1):
            max_val = 0
            max_val_index = 0
            for j in range(1, arr[i]+1):
                if arr[j+i]+j > max_val:
                    max_val = arr[i + j] + j
                    max_val_index = i+j
            i = max_val_index
            steps += 1
        return steps+1
        
def jump(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 0
        
        if(nums[0] >= len(nums)-1):
            return 1

        jumps = 0
        max_index = 0

        while(max_index<len(nums)-1):
            temp_index = 0
            max_sum = 0
            for i in range(max_index+1,max_index+nums[max_index]+1):
                sum_i = i+nums[i]
                if(sum_i>=max_sum):
                    temp_index = i
                    max_sum = sum_i
            max_index = temp_index
            jumps += 1
            if(max_sum>=len(nums)-1):
                return jumps+1
"""

"""
Method 2: Dynamic Programming. 
In this method, we build jumps[] array from right to left such that 
jumps[i] indicates the minimum number of jumps needed to reach arr[n-1] from arr[i]. 
Finally, we return jumps[0].

Time complexity:O(n^2). 
Nested traversal of the array is needed.
Auxiliary Space:O(n). 
To store the DP array linear space is needed. 
"""
# Python3 program to find Minimum
# number of jumps to reach end

# Returns Minimum number of
# jumps to reach end
def minJumps(arr, n):

    # jumps[0] will hold the result
    jumps = [0 for i in range(n)]

    # Minimum number of jumps needed
    # to reach last element from
    # last elements itself is always 0
    # jumps[n-1] is also initialized to 0

    # Start from the second element,
    # move from right to left and
    # construct the jumps[] array where
    # jumps[i] represents minimum number
    # of jumps needed to reach arr[m-1]
    # form arr[i]
    for i in range(n-2, -1, -1):

        # If arr[i] is 0 then arr[n-1]
        # can't be reached from here
        if (arr[i] == 0):
            jumps[i] = float('inf')

        # If we can directly reach to
        # the end point from here then
        # jumps[i] is 1
        elif (arr[i] >= n - i - 1):
            jumps[i] = 1

        # Otherwise, to find out the
        # minimum number of jumps
        # needed to reach arr[n-1],
        # check all the points
        # reachable from here and
        # jumps[] value for those points
        else:
            # initialize min value
            min = float('inf')

            # following loop checks with
            # all reachable points and
            # takes the minimum
            for j in range(i + 1, n):
                if (j <= arr[i] + i):
                    if (min > jumps[j]):
                        min = jumps[j]

            # Handle overflow
            if (min != float('inf')):
                jumps[i] = min + 1
            else:
                # or INT_MAX
                jumps[i] = min

    return jumps[0]

# Driver program to test above function
arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
n = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, n-1))



