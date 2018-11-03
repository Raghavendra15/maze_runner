from pathGenerator import *
import collections
from Analyzer import *
import datetime

class DFSWithoutHeuristics:
    x_cord = [0,1,0,-1] #[-1,0,1,0]
    y_cord = [1,0,-1,0]#[0,-1,0,1]
    path={}

    def __init__(self,matrix, startX, startY,goalX,goalY,grid,n,size,probability):
        self.grid = grid
        self.x = startX
        self.y = startY
        self.goal_x = goalX
        self.goal_y = goalY
        self.matrix = matrix
        self.size = n
        self.grid_size = size
        self.path[(startX,startY)] = None
        self.stack = []
        self.pathCount=0
        self.nodeExplored = 0
        self.isMazeSolved = False
        self.probability = probability


    def dfs(self,visited,x,y,p):
        visited[self.x][self.y] = 1
        self.stack.append((self.x,self.y))
        while self.stack:
            x,y=self.stack.pop()

            self.nodeExplored += 1
            #p.mark_path(x, y)
            for i in range(0,4):
                x_temp = DFSWithoutHeuristics.x_cord[i] + x
                y_temp = DFSWithoutHeuristics.y_cord[i] + y
                if (x_temp >=0 and x_temp < self.size and y_temp >=0 and y_temp <self.size
                    and visited[x_temp][y_temp] == 0 and self.matrix[x_temp][y_temp]==1):
                    self.path[(x_temp,y_temp)]=(x,y)
                    visited[x_temp][y_temp] = 1
                    if x_temp == self.goal_x and y_temp == self.goal_y:
                        return True
                    self.stack.append((x_temp,y_temp))
        return False

    def dfsUtil(self):
        visited = [[0 for x in range(self.size)] for y in range(self.size)]
        p = PathGenerator(self.grid,self.grid_size)
        self.isMazeSolved=self.dfs(visited,self.x,self.y,p)
        if self.isMazeSolved:
            self.getPath(self.goal_x,self.goal_y)

    def solve(self):
        old_time = datetime.datetime.now()
        print(old_time)
        self.dfsUtil()
        new_time = datetime.datetime.now()
        print(new_time)
        print((new_time - old_time).total_seconds())
        print("********************")
        print(self.nodeExplored)
        return Analyzer(self.matrix,0,self.nodeExplored,len(self.stack),(new_time - old_time).total_seconds(),self.isMazeSolved)


    def getPath(self,x,y):
        while (self.path[(x,y)]!= None):
            self.pathCount=self.pathCount+1
            x,y=self.path[(x,y)]
        print(self.pathCount)
        return self.pathCount



