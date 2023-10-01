'''
You are given data structure of a person and his busy time. You need to return all the possible time slots and person who is busy in that.

e.g.
Person name Start time End time
A 10 50
B 30 70
C 40 80
D 10 20

Output:
10-20 -> A, D
20-30 -> A (Note: this time slot was not given in input. You need to find it out.)
30-50 -> A, B, C
50-70 -> B,C
70-80 -> C
'''
import collections
inputs={'Matt':[3,8],'julia':[7,10], 'me':[3,6]}

time=collections.defaultdict(lambda: [set(),set()])
for p,[start,end] in inputs.items():
    time[start][0].add(p)
    time[end][1].add(p)
    
cur,t=set(), sorted(time)   
 
for t1,t2 in zip(t[:-1],t[1:]):  
    cur=(cur|time[t1][0])-time[t1][1]
    print(['{}-{} {}'.format(t1,t2,' '.join(cur))])   