#14500 테트로미노
import sys
n,m=map(int,input().split())
tetromino=[[[0,0],[0,1],[0,2],[0,3]],[[0,0],[0,1],[1,0],[1,1]],[[0,0],[1,0],[2,0],[3,0]],
           [[0,0],[1,0],[2,0],[2,1]],[[0,0],[1,0],[2,0],[2,-1]],[[0,0],[1,0],[2,0],[0,1]],[[0,0],[1,0],[2,0],[0,-1]],
           [[0,0],[1,0],[0,1],[0,2]],[[0,0],[1,0],[1,1],[1,2]],[[0,0],[-1,0],[0,-1],[0,-2]],[[0,0],[1,0],[0,-1],[0,-2]],
           [[0,0],[1,0],[1,1],[2,1]],[[0,0],[0,1],[-1,1],[-1,2]],[[0,0],[1,0],[0,1],[-1,-1]],[[0,0],[0,-1],[1,0],[1,1]],
           [[0,0],[1,0],[0,1],[0,-1]],[[0,0],[1,0],[1,-1],[1,1]],[[0,0],[-1,0],[1,0],[0,-1]],[[0,0],[0,1],[-1,0],[1,0]]]
graph=[]
res=0
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        for k in range(len(tetromino)):
            temp_sum=0
            for l in range(len(tetromino[k])):
                try:
                    temp_sum+=(graph[i+tetromino[k][l][0]][j+tetromino[k][l][1]])
                except:
                    temp_sum=0
                    break
            if res<temp_sum:
                res=temp_sum
print(res)