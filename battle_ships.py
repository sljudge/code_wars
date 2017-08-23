import itertools

def damaged_or_sunk (board, attacks):
    '''
    - 1 point for every whole boat sank.
    - 0.5 points for each boat hit at least once (not including boats that are sunk).
    - -1 point for each whole boat that was not hit at least once.
    
    - sunk = all boats that are sunk
    - damaged = all boats that have been hit at least once but not sunk
    - notTouched/not_touched = all boats that have not been hit at least once
    
    `sunk`, `damaged`, `not_touched`, `points`
    '''
                
    #{ 'sunk': 0, 'damaged': 2 , 'not_touched': 1, 'points': 0 }
    
    result = {'sunk':0, 'damaged':0, 'not_touched':0, 'points':0}
    
    damaged_boats = []
    untouched_boats = []
    sunk_boats = []
    
    # Damaged and Sunk Boats
    for x in attacks:
        if board[-x[1]][x[0]-1] > 0:
            if board[-x[1]][x[0]-1] not in damaged_boats:
                damaged_boats.append(board[-x[1]][x[0]-1])
                result['damaged'] += 1
            temp = int(board[-x[1]][x[0]-1])
            board[-x[1]][x[0]-1] = 0
            if temp not in (list(itertools.chain.from_iterable(board))):
                sunk_boats.append(temp)
                result['sunk'] += 1
                result['damaged'] -= 1
    
    # Untouched Boats
    for x in board:
        for y in x:
            if y > 0 and y not in damaged_boats and y not in untouched_boats:
                untouched_boats.append(y)
                result['not_touched'] += 1
    
    
    print(sunk_boats)
    # Points 
    for boat in damaged_boats:
        if boat not in sunk_boats:
            result['points'] += 0.5
    for boat in sunk_boats:
        result['points'] += 1
    for boat in untouched_boats:
        result['points'] -= 1
    
                
    return result
 
 
 
board = [   [0, 0, 1, 0], 
            [0, 0, 1, 0],  
            [0, 0, 1, 0]    ]

                
attacks = [[3, 1], [3, 2], [3, 3]]
    

print(damaged_or_sunk(board,attacks))









