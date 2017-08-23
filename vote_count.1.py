
def runoff(voters):
    '''
    instant runoff voting
    eg:
    voters =[   ["dem", "ind", "rep"],
                ["rep", "ind", "dem"],
                ["ind", "dem", "rep"],
                ["ind", "rep", "dem"]]

    Test.assert_equals(runoff(voters), "ind")
    '''
    votes = {}
    
    # Tally votes
    for ballot in voters:
        try:
            votes[ballot[0]] += 1
        except KeyError:
            votes[ballot[0]] = 1
    print(votes)
    
    # Discard candidates that receive no first choices
    for y in range(len(voters)):
        voters[y] = list(filter(lambda x: x in votes.keys() , voters[y]))
    
    # Is there a winner?
    for x in votes:
        if votes[x] > sum(votes.values()) / 2:
            return x
    
    # Find candidate with fewest votes
    candidate, lowest_score = min(votes.items(), key=lambda x:x[1])
    
    # Is there a tie?
    if all(x == lowest_score for x in list(votes.values())):
        return None
    # Eliminate candidate(s) with fewest votes
    else:
        for ballot in voters:
            if votes[ballot[0]] == lowest_score:
                ballot.remove(ballot[0])
        print(voters)

    return runoff(voters)
    
   



voters = [  ['a', 'c', 'b', 'd', 'e'], 
            ['d', 'c', 'a', 'b', 'e'], 
            ['e', 'b', 'd', 'a', 'c'], 
            ['e', 'a', 'b', 'c', 'd'], 
            ['b', 'c', 'e', 'a', 'd']]

print(runoff(voters))