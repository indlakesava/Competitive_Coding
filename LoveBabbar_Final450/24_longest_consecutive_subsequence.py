"""
Method-1:
for each element check if its the starting element by checking if its previous element is not in the list
Then start proceeding further and keep counting. Once you reach end of that sequence then check with the final maximum_length
Time Complexity: O(n)
Space Complexity: O(n)
"""

def longestConsecutive(nums):
	numset = set(nums)
	max_length = 0
	for i in nums:
		temp_length = 0
		if i-1 not in numset:
			temp_length = 1
			while(i+temp_length in numset):
				temp_length += 1
			max_length = max(temp_length, max_length)
	return max_length

print(longestConsecutive([100, 4, 200, 1, 3, 2]))