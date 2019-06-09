print("Enter comma seperated values:")
l = list(map(int,input().split(','))
for i in l:
  if i>237:
    break
  if i%2==0:
    print(i)
