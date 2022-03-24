def solution(citations):

    cit = sorted(citations, reverse=True)
    
    for h in range(min(cit[0], len(cit)), 0, -1):
        if len([_ for _ in cit if _ >= h]) >= h:
            return h

    return 0