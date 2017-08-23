def original_number(s):
    '''
    For s = "ONE", the output should be 1.

    For s = "EON", the output should be 1 too.

    For s = "ONETWO", the output should be 12.

    For s = "OONETW", the output should be 12 too.

    For s = "ONETWOTHREE", the output should be 123.

    For s = "TTONWOHREEE", the output should be 123 too.
    '''
    '''                                         KEY
    ZERO -  4   -   Z   -       -               Z
    ONE -   3   -       -       -   ON          O-N
    TWO -   3   -   W   -       -               W
    THREE - 5   -       -   H   -               H
    FOUR -  4   -   U   -       -               U
    FIVE-   4   -       -   V   -   I           I-V
    SIX -   3   -   X   -       -               X
    SEVEN - 5   -       -   V   -   N           V-N
    EIGHT - 5   -   G   -       -               G
    NINE-   4   -       -       -   IN          I-N
    '''
    from collections import Counter
    
    numbers = []
    letters = list(s)

    
    while len(letters) > 0:
        if "Z" in letters:
            letters = list((Counter(letters) - Counter("ZERO")).elements())
            numbers.append(0)
        elif "W" in letters:
            letters = list((Counter(letters) - Counter("TWO")).elements())
            numbers.append(2)
        elif "U" in letters:
            letters = list((Counter(letters) - Counter("FOUR")).elements())
            numbers.append(4)
        elif "X" in letters:
            letters = list((Counter(letters) - Counter("SIX")).elements())
            numbers.append(6)
        elif "G" in letters:
            letters = list((Counter(letters) - Counter("EIGHT")).elements())
            numbers.append(8)
        elif "H" in letters:
            letters = list((Counter(letters) - Counter("THREE")).elements())
            numbers.append(3)
        elif "V" in letters and "F" in letters:
            letters = list((Counter(letters) - Counter("FIVE")).elements())
            numbers.append(5)
        elif "V" in letters and "S" in letters:
            letters = list((Counter(letters) - Counter("SEVEN")).elements())
            numbers.append(7)
        elif "I" in letters:
            letters = list((Counter(letters) - Counter("NINE")).elements())
            numbers.append(9)
        elif "O" in letters:
            letters = list((Counter(letters) - Counter("ONE")).elements())
            numbers.append(1)
    
    print (numbers)
    numbers = map(str,numbers)
    return ''.join(sorted(numbers))





s = "TTONWOHREEE"
print(original_number(s))

# ALTERNATE EXAMPLES
# def original_number(s):
#     # Count occurences of numbers
#     n0 = s.count('Z')                # Count the number of Z's in s for 0
#     n2 = s.count('W')                # Count the number of W's in s for 2
#     n8 = s.count('G')                # Count the number of G's in s for 8
#     n3 = s.count('T') - n2 - n8      # Threes = T's in s - 2's - 8's
#     n4 = s.count('R') - n0 - n3      # Fours  = R's in s - 0's - 3's
#     n1 = s.count('O') - n0 - n2 - n4 # Ones = O's in s - 0's - 2's - 4's
#     n5 = s.count('F') - n4           # Fives = F's in s - 4's
#     n6 = s.count('X')                # Count the number of X's in s for 6
#     n7 = s.count('V') - n5           # Sevens = V's in s - 5's
#     n9 = s.count('I') - n5 - n6 - n8 # Nines = N's in s - 1's - 7's
    
#      # Append numbers
#     return '0'*n0 + '1'*n1 + '2'*n2 + '3'*n3 + '4'*n4 + '5'*n5 + '6'*n6 + '7'*n7 + '8'*n8 + '9'*n9

# *****************************************************
# from collections import Counter 

# EXECUTIONS_ORDER = [('Z', Counter("ZERO"),  '0'),
#                     ('W', Counter("TWO"),   '2'),
#                     ('U', Counter("FOUR"),  '4'),
#                     ('X', Counter("SIX"),   '6'),
#                     ('G', Counter("EIGHT"), '8'),
#                     ('O', Counter("ONE"),   '1'),
#                     ('H', Counter("THREE"), '3'),
#                     ('F', Counter("FIVE"),  '5'),
#                     ('V', Counter("SEVEN"), '7'),
#                     ('I', Counter("NINE"),  '9')]

# def original_number(s):
#     ans, count, executions = [], Counter(s), iter(EXECUTIONS_ORDER)
#     while count:
#         c, wordCount, value = next(executions)
#         ans.extend([value]*count[c])
#         for _ in range(count[c]): count -= wordCount
#     return ''.join(sorted(ans))