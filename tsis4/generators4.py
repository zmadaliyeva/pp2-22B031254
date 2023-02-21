def square(start,end):
    for i in range(start,end):
        yield i**2

a=int(input())
b=int(input())

for num in square(a,b):
    print(num)