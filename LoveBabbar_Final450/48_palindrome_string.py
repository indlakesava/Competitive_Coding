"""
Method-1
2 pointer
Time Complexity: O(n)
Space Complexity: O(1)
"""
def isPalindrome(S):
	# code here
	for i in range(len(S)//2):
		if S[i]!=S[len(S)-i-1]:
			return False
	else:
		return True

print(isPalindrome('abcba'))

