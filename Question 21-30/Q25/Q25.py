import itertools

class submission:
    def __init__(self, problem=0, score=0):
        self.problem = problem
        self.score = score
    
T = int(input())

for i in range(T):
    N = int(input())
    l = []
    for j in range(N):
        problem, score = tuple(map(int, input().split()))
        l.append(submission(problem, score))
    
    # created a hash table for with the problem number and total score which is initially at zero (0)
    d = dict()
    for key, value in zip(range(1,9),itertools.repeat(0,8)):
        d[key] = value
    
    # checking if the score on hash table is less that the current score or not. If it is less then change the value in hash table
    for sub in l:
        if sub.problem<=8 and d[sub.problem]<sub.score:
            d[sub.problem] = sub.score
    
    print(sum(d.values()))