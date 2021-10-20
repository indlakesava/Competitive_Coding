#Time Complexity = O(m + n)
"""
Union of arrays arr1[] and arr2[]

To find union of two sorted arrays, follow the following merge procedure :

1) Use two index variables i and j, initial values i = 0, j = 0
2) If arr1[i] is smaller than arr2[j] then print arr1[i] and increment i.
3) If arr1[i] is greater than arr2[j] then print arr2[j] and increment j.
4) If both are same then print any of them and increment both i and j.
5) Print remaining elements of the larger array.
"""

def printUnion(arr1, arr2, m, n):
    union = []
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            union.append(arr2[j])
            j+= 1
        else:
            union.append(arr2[j])
            j += 1
            i += 1

    # Print remaining elements of the larger array
    while i < m:
        union.append(arr1[i])
        i += 1

    while j < n:
        union.append(arr2[j])
        j += 1

    return union
# Driver program to test above function
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
printUnion(arr1, arr2, m, n)

"""
Intersection of arrays arr1[] and arr2[]

To find intersection of 2 sorted arrays, follow the below approach : 
1) Use two index variables i and j, initial values i = 0, j = 0 
2) If arr1[i] is smaller than arr2[j] then increment i. 
3) If arr1[i] is greater than arr2[j] then increment j. 
4) If both are same then print any of them and increment both i and j.
"""

# Python program to find intersection of
# two sorted arrays
# Function prints Intersection of arr1[] and arr2[]
# m is the number of elements in arr1[]
# n is the number of elements in arr2[]
def printIntersection(arr1, arr2, m, n):
    intersection = []
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j+= 1
        else:
            intersection.append(arr2[j])
            j += 1
            i += 1

    return intersection
# Driver program to test above function
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
printIntersection(arr1, arr2, m, n)

