import random
from DFS import *
from BFS import *
from AStar import *
from GridGenerator import *
from graphics import *
from Utility import *
from GeneticAlgorithm import *
from DFSWithoutHeuristics import *
from Analyzer import *
import pandas as pd

size = 20
startX = 0
startY = 0
n = 10
itr = 1
analyzerObjectDFS = []
analyzerObjectBFS=[]
analyzerObjectAStar= []
analyzerObjectAStarMan= []
count = 0
plist=[]
p=0.2
Matrix = Utility.matrixGenerator(n,p)
gridObj = GridGenerator(Matrix,"BFS")
grid=gridObj.generate_grid(n,size)

analyseBFS=DFS(Matrix, startX, startY ,n-1,n-1,grid,n,size,p).solve().to_dict()
    #AStar(Matrix, startX, startY, n - 1, n - 1, grid, n, size, p, "Eucledian").solve().to_dict()
print("Analyse BFS ####### SP",analyseBFS['Shortest Path'])
grid.getMouse()
grid.close()