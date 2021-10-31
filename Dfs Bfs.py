from sys import stdin, stdout 
from collections import defaultdict as D
from collections import deque
def II():
	return map(int,input().split())
def ii():
	return int(input())
def infi():
    return float("Inf")
def mino():
    return -1
class Graph: 
    def __init__(self):
        self.graph = D(list)
        self.Time=0
    
    def addEdge(self, v, w):
        self.graph[v].append(w)
    def BFS(self,u):
        qu=deque()
        qu.append(u)
        self.visited[u]=True
        x=[]
        while qu:
            s=qu.popleft()
            x.append(s)
            for i in self.graph[s]:
                if self.visited[i]==0:
                    qu.append(i)
                    self.visited[i]=True
    def Bfs(self,n):
        self.c=0
        self.visited=D(int)
        for i in range(1,n+1):
            if not self.visited[i]:
                self.BFS(i)
                self.c+=1
    def DFSt(self, s):
        stack=[s]
        self.dpt[s]=1
        self.prev[s]=-1
        while len(stack)!=0:
            s=stack.pop()
            if not self.visited[s]:
                
                for i in self.graph[s]:
                    if not self.visited[i]:
                        stack.append(i)
                        self.prev[i]=s
                        self.dpt[i]=self.dpt[s]+1
            self.visited[s]=1
    def DFS(self):
        self.visited=D(int)
        self.dpt=D(int)
        self.prev=D(bool)
        for i in self.graph:
            if not self.visited[i]:
                self.DFSt(i)

def dfs1(g):
    n=len(g)
    visited=[False]*n
    pointer=[0]*n
    prev=[None]*n
    order=[]
    for x in range(n):
        if not visited[x]:
            stack=[x]
            visited[x]=True
            while stack:
                y=stack[-1]
                any_more=False
                for i in range(pointer[y],len(g[y])):
                    s=g[y][i]
                    pointer[y]+=1
                    if not visited[s]:  
                        stack.append(s)
                        visited[s]+=1
                        prev[s]=y
                        any_more=True
                        break
                if not any_more:
                    order.append(y)
                    stack.pop()
    return order
def dfs2(gt,g,order):
    visited=[False]*n
    pointer=[0]*n
    prev=[None]*n
    tscc=0
    for k in range(len(order)-1,-1,-1):
        x=order[k]
        if not visited[x]:
            stack=[x]
            visited[x]=True
            scc=0
            while stack:
                y=stack[-1]
                any_more=False
                for i in range(pointer[y],len(g[y])):
                    s=g[y][i]
                    pointer[y]+=1
                    if not visited[s]:  
                        stack.append(s)
                        visited[s]+=1
                        any_more=True
                        break
                if not any_more:
                    scc+=1
                    stack.pop()
            
            if scc!=1:
                tscc+=scc
            elif len(gt[x])==0:
                tscc+=scc
            
    return tscc
'''n,m=n
g=[[] for i in range(n)]
gt=[[] for i in range(n)]
for i in range(m):
    x,y=[int(x) for x in stdin.readline().split()]
    g[x-1].append(y-1)
    gt[y-1].append(x-1)
x=dfs1(g)
z=dfs2(g,gt,x)
stdout.write(str(z)+"\n")'''
    
def Bri(g,m):
    n=len(g)
    visited=[False]*n
    pointer=[0]*n
    disc=[0]*n
    low=[float('inf')]*n
    prev=[None]*n
    stack=[0]
    children=[[] for i in range(n)]
    Time=0
    is_bridge=[False]*m
    for x in range(n):
        if not visited[x]:
            stack=[x]
            visited[x]=True
            disc[x]=Time
            low[x]=Time
            while stack:
                y=stack[-1]
                any_more=False
                for i in range(pointer[y],len(g[y])):
                    s,z=g[y][i]
                    pointer[y]+=1
                    if not visited[s]:  
                        stack.append(s)
                        Time+=1
                        disc[s]=Time
                        visited[s]+=1
                        prev[s]=y
                        children[y].append((s,z))
                        any_more=True
                        break
                    elif prev[y]!=s:
                        low[y]=min(low[y],disc[s])
                if not any_more:
                    for s,z in children[y]:
                        low[y]=min(low[y],low[s])
                        if low[s]>disc[y]:
                            
                            is_bridge[z]=True
                    stack.pop()
    return is_bridge
            

n,m,q=[int(x) for x in stdin.readline().split()]
g=[[] for i in range(n)]

for i in range(m):
    x,y,z=[int(x) for x in stdin.readline().split()]
    g[x-1].append((y-1,z-1))
    g[y-1].append((x-1,z-1))
x=Bri(g,m)
for i in range(q):
    z=int(stdin.readline().strip())-1
    if x[z]:
        stdout.write("YES\n")
    else:
        stdout.write("no\n")
