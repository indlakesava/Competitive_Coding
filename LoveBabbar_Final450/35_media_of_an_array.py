"""
Method-1: Naive Approach
Sort the array arr[] in increasing order.
If number of elements in arr[] is odd, then median is arr[n/2].
If the number of elements in arr[] is even, median is average of arr[n/2] and arr[n/2+1].

Time Complexity: O(nlog(n))
Space Complexity: O(1)
"""

import math

def find_median(v):
	# Code here
	v.sort()
	mid = len(v)//2
	if(len(v)%2==0):
		return math.floor((v[mid-1]+v[mid])/2)
	else:
		return v[mid]

print(find_median([90, 100, 78, 89, 67]))
print(find_median([56, 67, 30, 79]))

"""
Method-2:
Efficient Approach: using Randomized QuickSelect  

. 	Randomly pick pivot element from arr[] and the using the partition step from the quick sort algorithm 
	arrange all the elements smaller than the pivot on its left and the elements greater than it on its right.
.	If after the previous step, the position of the chosen pivot is the middle of the array then it is the 
	required median of the given array.
.	If the position is before the middle element then repeat the step for the subarray starting from 
	previous starting index and the chosen pivot as the ending index.
.	If the position is after the middle element then repeat the step for the subarray starting from 
	the chosen pivot and ending at the previous ending index.
.	Note that in case of even number of elements, the middle two elements have to be found and their average 
	will be the median of the array.

Time Complexity: 
Best case analysis: O(1)
Average case analysis: O(N)
Worst case analysis: O(N2)
Auxiliary Space: O(N)
"""
# Python3 program to find median of
# an array
import random

a, b = None, None;

# Returns the correct position of
# pivot element
def Partition(arr, l, r) :

    lst = arr[r]; i = l; j = l;
    while (j < r) :
        if (arr[j] < lst) :
            arr[i], arr[j] = arr[j],arr[i];
            i += 1;

        j += 1;

    arr[i], arr[r] = arr[r],arr[i];
    return i;

# Picks a random pivot element between
# l and r and partitions arr[l..r]
# around the randomly picked element
# using partition()
def randomPartition(arr, l, r) :
    n = r - l + 1;
    pivot = random.randrange(1, 100) % n;
    arr[l + pivot], arr[r] = arr[r], arr[l + pivot];
    return Partition(arr, l, r);

# Utility function to find median
def MedianUtil(arr, l, r,
                k, a1, b1) :

    global a, b;

    # if l < r
    if (l <= r) :

        # Find the partition index
        partitionIndex = randomPartition(arr, l, r);

        # If partition index = k, then
        # we found the median of odd
        # number element in arr[]
        if (partitionIndex == k) :
            b = arr[partitionIndex];
            if (a1 != -1) :
                return;

        # If index = k - 1, then we get
        # a & b as middle element of
        # arr[]
        elif (partitionIndex == k - 1) :
            a = arr[partitionIndex];
            if (b1 != -1) :
                return;

        # If partitionIndex >= k then
        # find the index in first half
        # of the arr[]
        if (partitionIndex >= k) :
            return MedianUtil(arr, l, partitionIndex - 1, k, a, b);

        # If partitionIndex <= k then
        # find the index in second half
        # of the arr[]
        else :
            return MedianUtil(arr, partitionIndex + 1, r, k, a, b);

    return;

# Function to find Median
def findMedian(arr, n) :
    global a;
    global b;
    a = -1;
    b = -1;

    # If n is odd
    if (n % 2 == 1) :
        MedianUtil(arr, 0, n - 1, n // 2, a, b);
        ans = b;

    # If n is even
    else :
        MedianUtil(arr, 0, n - 1, n // 2, a, b);
        ans = (a + b) // 2;

    # Print the Median of arr[]
    print("Median = " ,ans);


# Driver code
arr = [ 12, 3, 5, 7, 4, 19, 26 ];
n = len(arr);
findMedian(arr, n);

