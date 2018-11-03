import random
import numpy as np
from DFS import *
from BFS import *
from AStar import *

class Utility:

   @staticmethod
   def shuffle(matrix):
       n=len(matrix)
       np.random.shuffle(matrix)
       matrix[0][0]=1
       matrix[n-1][n-1]=1
       return matrix

   @staticmethod
   def performMutation(self):
       print("gautam")

   @staticmethod
   def performCrossOver(self):
       print("yes")

   @staticmethod
   def matrixGenerator(n,p):
        Matrix = [[0 for x in range(n)] for y in range(n)]
        for i in range(0, n, 1):
            for j in range(0, n, 1):
                prob = random.random()
                if prob > p:
                    Matrix[i][j] = 1
        Matrix[n-1][n-1] = 1
        Matrix[0][0]=1
        return Matrix

   @staticmethod
   def getAlgo(type,Matrix,startX,startY,n,grid,size):
       if type=="DFS":
           print("DFS")
           result=DFS(Matrix, startX, startY, n - 1, n - 1, grid, n, size)

           return result
       if type=="BFS":
           return BFS(Matrix,startX,startY,n-1,n-1,grid,n,size)
       if type == "AStar":
           return AStar(Matrix,startX,startY,n-1,n-1,grid,n,size,"Manhattan")