def my_range(a):
    for i in range(a):
        if i%2==0:
            yield i

        

a=int(input())
if a%2==0:
    x=a/2
else:
    x=int(a/2)+1
cnt=1
for num in my_range(a):
    if cnt==x:
        print(num)
        exit()
    else:
        print(num,end=',')
        cnt+=1