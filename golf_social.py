import collections 

def valid(schedule):
    '''
    takes proposed golfing schedule and asserts that:
    - each player plays once per day
    - the number and size of the groups is the same every day
    - each player plays with every other player at most once
    
    [
      ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],     Mon
      ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],     Tue
      ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],     Wed
      ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],     Thur
      ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']      Fri
    ]
            20                          4               5
    N = number of golfers || G = players per group || D = days
    '''
    record = {}
    N = 0
    G = len(schedule[0][0])
    try:
        # 0. Create record of first day of play and record number of golfers(N)
        for group in schedule[0]:
            for golfer in group:
                record[golfer] = []
                N += 1
        
        for day in schedule:
            day_total = 0
            for group in day:
                # 1. Check same group size(G)
                if len(group) > G:
                    return False
                else:
                    for golfer in group:
                        record[golfer].append(group)
                        day_total += 1
            # 2. Check same number of golfers per day    
            if day_total != N:
                return False
                    
                
        # 3. Check that each player plays with every other player at most once
        for golfer in record:
            test = ''.join(record[golfer]).replace(golfer,'')
            test = collections.Counter(test)
            for player in test:
                if test[player] > 1:
                    return False
                    
        return True
    
    except KeyError:
        return False

schedule =[ ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],     #Mon
            ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],     #Tue
            ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],     #Wed
            ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],     #Thur
            ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']    ]
print(valid(schedule))

# ALTERNATE SOLUTIONS

# def valid(a):   
#     d = {}
#     day_length = len(a[0])
#     group_size = len(a[0][0])
#     golfers = {g for p in a[0] for g in p}
    
#     for day in a:
#         if len(day) != day_length: return False
#         for group in day:
#             if len(group) != group_size: return False
#             for player in group:
#                 if player not in golfers: return False
#                 if player not in d:
#                     d[player] = set(group)
#                 else:
#                     if len(d[player] & set(group)) > 1: return False
#                     else: d[player].add(group)
#     return True