def reverse(lst):
    i = 0
    j = len(lst)-1

    while(i<j):
        lst[i],lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

    return lst

l = [2,5,3,6,2,1,4]
print(l)
print(reverse(l))