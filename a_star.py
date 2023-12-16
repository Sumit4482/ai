# A* search strategy for shortest path in a graph
n=int(input("Enter the number of nodes: "))
print("Enter the adjacency matrix: ")
a=[]
for i in range(n):
    a.append([int(j) for j in input().split()])
s=int(input("Enter the source vertex: "))
d=int(input("Enter the destination vertex: "))
print("enter the heuristic values: ")
h=[int(i) for i in input().split()]
v=[0 for i in range(n)]
v[s-1]=1
p=[s]
c=0
while True:
    m=1000
    for i in range(n):
        if a[s-1][i]!=0 and v[i]==0:
            if m>h[i]:
                m=h[i]
                t=i+1
    c+=a[s-1][t-1]
    s=t
    v[s-1]=1
    p.append(s)
    if s==d:
        break
print("The shortest path is: ")
print(p)
print("The cost of the path is: ",c)

