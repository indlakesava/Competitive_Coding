"""
Method-1:
Traverse through all the elements
Time COmplexity: O(m*n)
"""
def rowWithMax1s(arr, n, m):
	# code here
	overall_count = 0
	max_row = 0
	for i in range(n):
		temp_count = 0
		for j in range(m):
			if arr[i][j] == 1:
				temp_count += 1
		if temp_count>overall_count:
			overall_count = temp_count
			max_row = i
	if overall_count == 0:
		return -1
	return max_row

arry = [[0, 1, 1, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
print(rowWithMax1s(arry, 4, 4))