def bs(a, l, r, x): 
  while l <= r: 
     mid = l + (r - l)/2
        if a[mid] == x: 
            return mid 
        elif a[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1
    return -1
a = list(map(int,input().split(",")))
x = int(input("enter key:"))
a.sort()
c = bs(a,0,len(a)-1,x)
if c==-1:
  print("not present")
else:
  print("present at",c)
