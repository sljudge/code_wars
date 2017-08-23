def find_even_index(arr):
    '''
    1,2,3,4,3,2,1 => index 3 (1+2+3 =6= 3+2+1)
    1,100,50,-51,1,1 => index 1 (1 =1= 50-51+1+1)
    20,10,-80,10,10,15,35 => index 0 ([] =0= 10-80+10+10+15+35)
    '''
    def find_first_seg(x):
        total = 0
        for n in arr[0:x]:
            total += n
        return total
    
    def find_second_seg(x):
        total = 0
        for n in arr[x+1:]:
            total += n
        return total
    
    for x in range(len(arr)):
        first = find_first_seg(x)
        second = find_second_seg(x)
        if first == second:
            return x
    return -1

        
arr = [6,7,34,55,6]
print (find_even_index(arr))

# Alternate Solutions
# def find_even_index(arr):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return i
#     return -1
# ********************************************
# def find_even_index(lst):
#     left_sum = 0
#     right_sum = sum(lst)
#     for i, a in enumerate(lst):
#         right_sum -= a
#         if left_sum == right_sum:
#             return i
#         left_sum += a
#     return -1
    
    