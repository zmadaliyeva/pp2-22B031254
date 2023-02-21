def gensquares(s):
    for i in range(s + 1):
      yield i**2

x = int(input())
a = gensquares(x)
for i in a:
   print(i)
        