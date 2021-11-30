"""
Method 1:
Sorting and traversing
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

def merge(intervals):
	intervals.sort(key = lambda pair : pair[0])
	output = [intervals[0]]

	for start, end in intervals:
		lastEnd = output[-1][1]

		if start <= lastEnd:
			# merge
			output[-1][1] = max(lastEnd, end)
		else:
			output.append([start, end])

	return output

print(merge([[1,3],[2,6],[8,10],[15,18]]))