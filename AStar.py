from pathGenerator import *
from queue import PriorityQueue
import math
from Analyzer import *
import datetime

class Coord:
    def __init__(self,priority, x,y):
        self.priority = priority
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.priority < other.priority

class AStar:
    x_cord = [0, 1, 0, -1]
    y_cord = [1, 0, -1, 0]

    def __init__(self,matrix, startX, startY,goalX,goalY,grid,n,size,probability,type):
        self.grid = grid
        self.x = startX
        self.y = startY
        self.goal_x = goalX
        self.goal_y = goalY
        self.matrix = matrix
        self.size = n
        self.grid_size = size
        self.type = type
        self.map = {}
        self.pathCount = 0
        self.nodeExplored = 0
        self.isMazeSolved = False
        self.probability = probability
        self.queue = PriorityQueue()

    def distanceFromGoal(self,x1, y1):
         if self.type == "Manhattan":
            return abs(self.goal_x - x1) + abs(self.goal_y-y1)
         else:
             return  math.sqrt((self.goal_x - x1)**2 + (self.goal_y - y1)**2)

    def distanceFromSource(self,x_parent, y_parent,x_current,y_current):
        if self.map.get(tuple([x_current,y_current])) == None:
            self.map[tuple([x_current,y_current])] = self.map.get(tuple([x_parent,y_parent]))+1
        else:
            self.map[tuple([x_current,y_current])] = min(self.map.get(tuple([x_parent,y_parent]))+1, self.map.get(tuple([x_current,y_current])))
        return self.map.get(tuple([x_current,y_current]))

    def aStar(self,visited,x,y,p):
        self.queue.put(Coord(0,x,y))
        self.map[tuple([x,y])] = 0
        while not self.queue.empty():
            current_coord = self.queue.get()
            self.nodeExplored+=1
            if visited[current_coord.x][current_coord.y] ==1:

               continue
            #self.nodeExplored += 1

            visited[current_coord.x][current_coord.y] = 1
            # if not (current_coord.x == 0 and current_coord.y ==0):
            #     p.mark_path(current_coord.x, current_coord.y)
            for i in range(0,4):
                x_temp = AStar.x_cord[i] + current_coord.x
                y_temp = AStar.y_cord[i] + current_coord.y

                if x_temp == self.goal_x and y_temp == self.goal_y:
                    return True
                if (x_temp >=0 and x_temp < self.size and y_temp >=0 and y_temp <self.size
                    and visited[x_temp][y_temp] == 0 and self.matrix[x_temp][y_temp]==1):
                    #self.distanceFromSource(current_coord.x, current_coord.y, x_temp, y_temp)
                    self.queue.put(Coord((self.distanceFromGoal(x_temp,y_temp) ),x_temp,y_temp))
        return False

    def aStarUtil(self):
        visited = [[0 for x in range(self.size)] for y in range(self.size)]
        p = PathGenerator(self.grid,self.grid_size)
        self.isMazeSolved = self.aStar(visited, self.x, self.y, p)


    def solve(self):

        old_time = datetime.datetime.now()
        self.aStarUtil()
        new_time = datetime.datetime.now()
        print((new_time - old_time).total_seconds())
        print(self.nodeExplored)
        print(self.isMazeSolved)
        return Analyzer(self.matrix, self.nodeExplored, self.nodeExplored, self.queue.qsize(),
                        (new_time - old_time).total_seconds(), self.isMazeSolved, 'ASTAR', self.probability, self.size)
