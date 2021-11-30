"""
Method-1: Recursion
Time complexity: O(N)
So=pace Complexity: O(1)
"""

def fact(N):
	factorial = 1
	if N==0:
		factorial = 1
	else:
		factorial = N*fact(N-1)
	return factorial

print(fact(5))