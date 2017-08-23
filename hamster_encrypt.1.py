def hamster_me(code, message):
    '''
    1  | h a m s t e r      1  | a e h m r s t          1  | e h m r s t    
    2  | i b n   u f        2  | b f i n     u          2  | f i n     u
    3  | j c o   v g        3  | c g j o     v          3  | g j o     v
    4  | k d p   w          4  | d   k p     w          4  |   k p     w
    5  | l   q   x          5  |     l q     x          5  |   l q     x
    6  |         y          6  |             y          6  |           y
    7  |         z          7  |             z          7  |           z
                                                        8  |           a
    a => a1                                             9  |           b
    b => a2                                             10 |           c
    c => a3                                             11 |           d
    d => a4
    e => e1         hamsterMe('hamster', 'hamster')   => h1a1m1s1t1e1r1
    f => e2         hamsterMe('hamster', 'helpme')    => h1e1h5m4m1e1
                    hamsterMe('hmster', 'hamster')   => h1t8m1s1t1e1r1

    '''
    
    # Create key from code
    code = ''.join(sorted(code))
    i = 0
    key = []
    final_key = []
    
    # Key minus final key
    while i < len(code)-1:
        sub = []
        for x in range(ord(code[i]),ord(code[i+1])):
            sub.append(chr(x))
        key.append(sub)
        i += 1
    
    # Final key
    for x in range(ord(code[len(code)-1]),123):
        final_key.append(chr(x))
    for x in range(97,ord(code[0])):
        final_key.append(chr(x))
        
    key.append(final_key)

    # Apply key to message
    message_values = []
    for char in message:
        for sub in key:
            i = 0
            while i < len(sub):
                if char == sub[i]:
                    message_values.append((sub[0], str(i+1)))
                i += 1

    # Create string from message values
    result = []
    for sub in message_values:
        sub = ''.join(sub)
        result.append(sub)
    result = ''.join(result)
    return result
        
        

message = 'helpme'
code = 'hmster'
print(hamster_me(code, message))


 


    

    