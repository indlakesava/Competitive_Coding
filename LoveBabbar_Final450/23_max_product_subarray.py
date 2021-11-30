"""
Method-1: Traversal
The max_product can be either from start or end, not in between in case there is no 0.
if zero is present then we need to consider it as another array and do the same as above storing the earlier product
Time Complexity: O(n)
Space Complexity: O(1)
"""
# Function to find maximum
# product subarray
def maxProduct(arr):
	# code here
	final_product = arr[0]
	running_product = 1;
	for i in arr:
		running_product *= i
		final_product = max(final_product, running_product)
		if(running_product==0):
			running_product = 1

	running_product = 1;
	for i in arr[::-1]:
		running_product *= i
		final_product = max(final_product, running_product)
		if(running_product==0):
			running_product = 1

	return final_product

print(maxProduct([6, -3, -10, 0, 2]))