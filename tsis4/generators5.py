def gen(a):
    while a>=0:
        yield a
        a-=1
        
a=int(input())
for num in gen(a):
    print(num)
