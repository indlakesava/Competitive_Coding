"""
Method-1: Using Dictionary
Time complexity: O(n)
Space Complexity: O(n)
"""
def find_duplicates(s):
    d = {}
    lst = []
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for a,b in d.items():
        if b>1:
            lst.append(a)

    return lst

print(find_duplicates("test string"))