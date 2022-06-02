class pQ():
    def __init__(self):
        self.q = []
        
    def popleft(self):
        if self.q:
            return self.q.pop(0)
        else:
            return
    
    def pop(self):
        if self.q:
            return self.q.pop()
        else:
            return
    
    def append(self, val):
        st = 0
        ed = len(self.q)
        mid = (st + ed) // 2
        
        if ed == 0:
            self.q.append(val)
        else:
            while st < ed: 
                if self.q[mid] < val:
                    ed = mid
                else:
                    st = mid + 1
                mid = (st + ed) // 2
                
            self.q.insert(mid, val)

def solution(operations):
    answer = [0, 0]
    pq = pQ()
    
    for op in operations:
        com, num = op.split(" ")
        if com == 'I':
            pq.append(int(num))
        else: # D
            if num == "1":
                pq.popleft()
            else: # -1
                pq.pop()
    
    if pq.q:
        answer = [pq.q[0], pq.q[-1]]
    
    return answer