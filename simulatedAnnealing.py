
import Utility

class simulatedAnnealing:

    def __init__(self, matrix,startX,startY,goalX,goalY,iter):
        self.matrix=matrix
        self.x = startX
        self.y = startY
        self.goal_x = goalX
        self.goal_y = goalY
        self.iteration=iter
        self.analysis=None
        self.maxPath=0
        self.hardMatrix=None

    def perfomSimulation(self,matrix,startX,startY,n,grid,size):
        for i in range(self.iteration):
            self.analysis=Utility.getAlgo("DFS", matrix, startX, startY, n, grid, size)
            if(self.analysis.shortestPath> self.maxPath):
                self.maxPath=self.analysis.shortestPath
                self.hardMatrix=matrix
            else:
#
#                 array([[3, 2, 3, 3, 2],
#                        [2, 4, 2, 3, 4],
#                        [3, 1, 0, 1, 0],
#                        [3, 4, 4, 0, 4],
#                        [2, 4, 1, 2, 1]])
# array([[3, 2, 3, 3, 2],
#        [2, 4, 1, 2, 1],
#        [3, 1, 0, 1, 0],
#        [3, 4, 4, 0, 4],
#        [2, 4, 2, 3, 4]])