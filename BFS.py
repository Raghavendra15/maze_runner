from pathGenerator import *
from Analyzer import *
import datetime
class BFS:
    x_cord = [0, 1, 0, -1]
    y_cord = [1, 0, -1, 0]
    def __init__(self,matrix, startX, startY,goalX,goalY,grid,n,size,probability,f):
        self.grid = grid
        self.x = startX
        self.y = startY
        self.goal_x = goalX
        self.goal_y = goalY
        self.matrix = matrix
        self.size = n
        self.grid_size = size
        self.pathCount=0
        self.nodeExplored = 0
        self.isMazeSolved = False
        self.probability = probability
        self.queue = []
        self.f = f
        self.path = {}

    def bfs(self,visited,x,y,p):
        self.path[(x, y)] = None
        self.queue.append([x,y])
        visited[x][y] = 1
        while self.queue:
            d = self.queue.pop(0)
            #print("Queue Size:   ", len(self.queue))
            self.nodeExplored += 1
            if self.f and d[0] != 0 and d[1] !=0:
               p.mark_path(d[0], d[1])
            for i in range(0,4):
                x_temp = BFS.x_cord[i] + d[0]
                y_temp = BFS.y_cord[i] + d[1]
                if x_temp == self.goal_x and y_temp == self.goal_y:
                    self.path[(x_temp, y_temp)] = (d[0], d[1])
                    return True
                if (x_temp >=0 and x_temp < self.size and y_temp >=0 and y_temp <self.size
                        and visited[x_temp][y_temp] == 0 and self.matrix[x_temp][y_temp]==1):
                        #p.mark_path(x_temp,y_temp)
                        visited[x_temp][y_temp]=1
                        self.path[(x_temp, y_temp)] = (d[0], d[1])
                        self.queue.append([x_temp,y_temp])
        return False

    def bfsUtil(self):
        visited = [[0 for x in range(self.size)] for y in range(self.size)]
        p = PathGenerator(self.grid,self.grid_size)
        self.isMazeSolved = self.bfs(visited, self.x, self.y, p)
        if self.isMazeSolved:
            self.getPath(self.goal_x,self.goal_y)

    def solve(self):
        old_time = datetime.datetime.now()
        self.bfsUtil()
        new_time = datetime.datetime.now()
        return Analyzer(self.matrix, self.pathCount, self.nodeExplored, len(self.queue), (new_time - old_time).total_seconds(),self.isMazeSolved, 'BFS', self.probability, self.size)

    def getPath(self, x, y):
        while (self.path[(x, y)] != None):
            self.pathCount = self.pathCount + 1
            x, y = self.path[(x, y)]
        print(self.pathCount)
        return self.pathCount