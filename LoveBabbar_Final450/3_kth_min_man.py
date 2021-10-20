"""
Method 1:
A simple solution is to sort the given array using a O(N log N) sorting algorithm like
Merge Sort, Heap Sort, etc, and return the element at index k-1 in the sorted array.
Time Complexity of this solution is O(N Log N)
"""
def kth_min_by_sorting(nums, k):
    nums.sort()
    return nums[k-1]

lst = [2,5,3,6,1,4]
print('Kth Minimum element:', kth_min_by_sorting(lst, 3))


"""
Method 2
We can find k’th smallest element in time complexity better than O(N Log N). 
A simple optimization is to create a Min Heap of the given n elements and call extractMin() k times.
"""

""""
Method 3 (QuickSelect) 
This is an optimization over method 1 if QuickSort is used as a sorting algorithm in first step. 
In QuickSort, we pick a pivot element, then move the pivot element to its correct position and partition the surrounding array. 
The idea is, not to do complete quicksort, but stop at the point where pivot itself is k’th smallest element. 
Also, not to recur for both left and right sides of pivot, but recur for one of them according to the position of pivot. 
The worst case time complexity of this method is O(n2), but it works in O(n) on average. 
"""

# This function returns k'th smallest element
# in arr[l..r] using QuickSort based method.
# ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT

def kthSmallest(arr, l, r, k):
    # Partition the array around last element and get position of pivot element in sorted array
    pos = partition(arr, l, r)

    # If position is same as k
    if (pos - l == k - 1):
        return arr[pos]
    elif (pos - l > k - 1): # If position is more, recur for left subarray
        return kthSmallest(arr, l, pos - 1, k)
    else:
        return kthSmallest(arr, pos + 1, r, k - pos + l - 1)

# Standard partition process of QuickSort().
# It considers the last element as pivot and moves all smaller element to left of it and greater elements to right
def partition(arr, l, r):

    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

print('Kth Minimum element:', kthSmallest(lst, 0, len(lst)-1,3))