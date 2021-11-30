def rev_word(lst):
    i = 0
    j = 0
    while(i<=j):
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    print(lst)

    i, j = len(lst)-1, len(lst)-1
    while(i>0 and j>0):
        if(lst[j]==' '):
            lst = rev(lst, j+1, i)
            i=j-1
        j-=1
    lst = rev(lst, 0, i)
    return lst

def rev(s, i, j):
    while(i<=j):
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s

print(rev_word(['t','h','e',' ','s','k','y',' ','i','s',' ','b','l','u','e']))
"""
def partition(arr, l, r):
    i = l
    x = arr[r]
    for j in range(l, r):
        if arr[j]<=x:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i], arr[r] = arr[r], arr[i]
    return i
"""