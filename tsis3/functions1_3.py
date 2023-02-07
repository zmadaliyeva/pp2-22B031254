def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    if(heads>=legs):
        print(error_msg)
    elif(legs%2!=0):
        print(error_msg)
    else:
        rabbit_count=(legs-2*heads)/2
        chicken_count=heads-rabbit_count
        print(int(chicken_count),int(rabbit_count))
    
    #print(chicken_count,rabbit_count)
    #print(error_msg)

solve(35,94)


'''numheads = 35
numlegs = 94
def solve(numheads, numlegs):
    c_cnt = 0
    r_cnt = 0

    if(numheads>=numlegs) or (numlegs % 2 != 0):
        print('No solution')
    
    else:
        r_cnt = (numlegs-2*numheads)/2
        c_cnt = numheads - r_cnt
        print(int(c_cnt), int(r_cnt))
    
    print(c_cnt, r_cnt)
    #print()'''