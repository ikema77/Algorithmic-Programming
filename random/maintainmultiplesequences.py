N,Q = map(int,input().split())
L = [list(map(int, input().split()[1:])) for _ in range (N)]
s,t=[],[]
for _ in range(Q):
    val1,val2=map(int, input().split())
    s.append(val1)
    t.append(val2)

for i in range(Q):
    print(L[s[i]-1][t[i]-1])
