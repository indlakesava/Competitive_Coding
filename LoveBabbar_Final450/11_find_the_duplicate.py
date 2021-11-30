"""
Method 1: Using Dictionary
Space=O(n)
time=O(n)
"""

def findDuplicate(nums):
    d = {}
    for i in nums:
        if i in d:
            return i
        else:
            d[i] = 1

"""
Method 2: Mutable array
Space=O(n)
time=o(1)
"""
def findDuplicate(nums):
    for i in nums:
        if(nums[abs(i)])>0:
            nums[abs(i)] *= -1
        else:
            return abs(i)


"""
Method 3: Immutable array
Space=O(n)
time=o(1)
"""
def findDuplicate(nums):
# Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare



print(findDuplicate([3, 1, 3, 4, 2]))