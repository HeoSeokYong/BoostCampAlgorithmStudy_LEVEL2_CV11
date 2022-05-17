def solution(s):
    stack = []
    
    if len(s) % 2 != 0:
        return 0
    
    for w in s:
        if not stack:
            stack.append(w)
        elif stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    
    return 0 if stack else 1