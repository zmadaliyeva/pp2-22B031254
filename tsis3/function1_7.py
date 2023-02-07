def has_33(nums):
    my_list = []
    y =len(nums)-1
    for x in range(0,y) :
        if nums[x] == 3 and nums[x+1] == 3:
            my_list.append(1)
        else :
            my_list.append(0)
    print(my_list)
    if 1 in my_list:
        return True
    else :
        return False