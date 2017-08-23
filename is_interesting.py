def is_interesting(number,awesome_phrases):
    '''
    Any digit followed by all zeros: 100, 90000
    Every digit is the same number: 1111
    The digits are sequential, incementing: 1234
    The digits are sequential, decrementing: 4321
    The digits are a palindrome: 1221 or 73837
    The digits match one of the values in the awesome_phrases array
    For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
    For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
    The digits match one of the values in the awesome_phrases array.
    
     returns a 2 if the number is "interesting"
     1 if an interesting number occurs within the next two miles
     or a 0 if the number is not interesting.
     '''
    def all_zeros(number):
        for x in range(1,len(str(number))):
            if str(number)[x] in ['1','2','3','4','5','6','7','8','9']:
                return False
        return True
    
    def all_same(number):
        for x in range (len(str(number))):
            if str(number)[x] != str(number)[x-1]:
                return False
        return True

    def is_sequential_inc(number):
        temp = int(str(number)[0])
        for x in range(1,len(str(number))):
            if temp == 9 and str(number)[x] == '0':
              continue
            elif temp + 1 != int(str(number)[x]):
              return False
            temp = int(str(number)[x])
        return True
        
    def is_sequential_dec(number):
        temp = int(str(number)[0])
        for x in range(1,len(str(number))):
            if temp == 1 and str(number)[x] == '0':
              continue
            elif temp - 1 != int(str(number)[x]):
              return False
            temp = int(str(number)[x])
        return True
        
    def is_pal(number):
        if len(str(number)) <= 1:
            return True
        else:
            return int(str(number)[0]) == int(str(number)[-1]) and is_pal(str(number)[1:-1])
        
    # Check mileage under 100
    if number < 98:
        return 0
    elif number == 98 or number == 99:
        return 1
    
    # Check mileage over 100
    if all_zeros(number) or all_same(number) or is_sequential_inc(number) or is_sequential_dec(number) or is_pal(number):
        return 2
    elif number in awesome_phrases:
        return 2
    elif number + 1 in awesome_phrases or number + 2 in awesome_phrases:
        return 1
    elif all_zeros(number+1) or all_same(number+1) or is_sequential_inc(number+1) or is_sequential_dec(number+1) or is_pal(number+1):
        return 1
    elif all_zeros(number+2) or all_same(number+2) or is_sequential_inc(number+2) or is_sequential_dec(number+2) or is_pal(number+2):
        return 1
    else:
        return 0

# print(is_interesting(11207, [])) # 0
# print(is_interesting(11208, [])) # 0
# print(is_interesting(11209, [])) # 1
# print(is_interesting(11210, [])) # 1
# print(is_interesting(11211, [])) # 2

print(is_interesting(98, [])) # 0

# ALTERNATE SOLUTIONS
'''
def is_incrementing(number): return str(number) in '1234567890'
def is_decrementing(number): return str(number) in '9876543210'
def is_palindrome(number):   return str(number) == str(number)[::-1]
def is_round(number):        return set(str(number)[1:]) == set('0')

def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)
       
    for num, color in zip(range(number, number+3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0
'''
# *******************************************************
'''
def is_good(n, awesome):
    return n in awesome or str(n) in "1234567890 9876543210" or str(n) == str(n)[::-1] or int(str(n)[1:]) == 0

def is_interesting(n, awesome):
    if n > 99 and is_good(n, awesome):
        return 2
    if n > 97 and (is_good(n + 1, awesome) or is_good(n + 2, awesome)):
        return 1
    return 0
'''
# ********************************************************
