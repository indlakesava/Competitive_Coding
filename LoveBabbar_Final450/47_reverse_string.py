"""
Method-1: swap elements
Time Complexity: O(n)
Space Complexity: O(1)
"""
def reverseString(s):
    for i in range(len(s)//2):
        s[i], s[len(s)-i-1] =  s[len(s)-i-1], s[i]
    return s

print(reverseString(["h","e","l","l","o"]))

"""
Method-2: python builtin reverse 
"""
def reverse_string(s):
    return s[::-1]
print(reverse_string(["h","e","l","l","o"]))