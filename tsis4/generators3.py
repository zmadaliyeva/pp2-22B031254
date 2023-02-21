
'''def result(n):
 
    for num in range(n):
            
            if num % 3 == 0 and num % 4 == 0:
                print(str(num) + " ", end = "")
            
            else:
                pass
 
if __name__ == "__main__":
     
    n = int(input())
    result(n)'''
def gen(a):
    for i in range(a):
        if i%3==0 or i%4==0:
            yield i
    
a=int(input())
for num in gen(a):
    print(num)
    