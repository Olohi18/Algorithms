def some_function(a:list[int], x:int):
    l,m,n = 0, 0, len(a)-1
    while l <= n:
        m = (l+n)//2
        if x == a[m]:
            return m
        elif a[l] <= a[m]:
            if x > a[m]:
                l = m+1
            elif x >= a[l]:
                n = m-1
            else:
                l = m+1
        elif x < a[m]:
            n = m-1
        elif x <= a[n]:
            l = m+1
        else:
            n = m-1
    return -1

a:list[int] = [7, 8, 9, 6, 5]
print(some_function(a, 6))