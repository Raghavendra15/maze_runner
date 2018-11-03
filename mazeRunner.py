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

size = 6
startX = 0
startY = 0
n = 100
itr = 1
analyzerObjectDFS = []
analyzerObjectBFS=[]
analyzerObjectAStar= []
analyzerObjectAStarMan= []
count = 0
plist=[]
for i in range(10,60,1):
    p = i/100

    for j in range(itr):
       count+=1
       print(count)
       Matrix = Utility.matrixGenerator(n,p)
       gridObj = GridGenerator(Matrix,"DFS")
       grid = []#gridObj.generate_grid(n,size)
       ##gridObj1 = GridGenerator(Matrix,"BFS")
       ##grid1 = gridObj1.generate_grid(n,size)
       #gridObj2 = GridGenerator(Matrix,"AStar Euclidean")
       #grid2 = gridObj2.generate_grid(n,size)
       #gridObj3 = GridGenerator(Matrix,"AStar Manhatten")
       #grid3 = gridObj3.generate_grid(n,size)
       #print(Matrix)
       print("DFS")
       dfsNodesExp=[]
       analyseDFS=DFS(Matrix, startX, startY ,n-1,n-1,grid,n,size,p).solve().to_dict()
       if(analyseDFS['Maze Solved']==True):
            print("Maze solved DFS: ",analyseDFS['Maze Solved'])
            plist.append(analyseDFS['Probability'])
            dfsNodesExp.append(analyseDFS['Nodes Explored'])
            analyzerObjectDFS.append(analyseDFS)
       bfsNodesExp = []
       analyseBFS = BFS(Matrix, startX, startY, n - 1, n - 1, grid, n, size, p, False).solve().to_dict()
       if (analyseBFS['Maze Solved'] == True):
          print("Maze solved DFS: ", analyseBFS['Maze Solved'])

          bfsNodesExp.append(analyseBFS['Nodes Explored'])
          analyzerObjectBFS.append(analyseBFS)
       #nodesExpDFS=[]
       #nodesExpDFS.append(DFS(Matrix, startX, startY ,n-1,n-1,grid,n,size,p).solve().to_dict()['Nodes Explored'])
       #print("BFS")
       #analyzerObjectDFS.append(BFS(Matrix, startX, startY ,n-1,n-1,grid,n,size,p).solve().to_dict())
       #print("ASTAR EU")
       aStarNodesExp = []
       analyseAStar = AStar(Matrix, startX, startY ,n-1,n-1,grid,n,size,p,"Euclidean").solve().to_dict()
       if (analyseAStar['Maze Solved'] == True):
          print("Maze solved AStar: ", analyseAStar['Maze Solved'])
          aStarNodesExp.append(analyseAStar['Nodes Explored'])
          analyzerObjectAStar.append(analyseAStar)
       aStarMNodesExp = []
       analyseAStarM = AStar(Matrix, startX, startY, n - 1, n - 1, grid, n, size, p, "Manhattan").solve().to_dict()
       if (analyseAStarM['Maze Solved'] == True):
          print("Maze solved AStar Manhattan: ", analyseAStarM['Maze Solved'])
          aStarMNodesExp.append(analyseAStarM['Nodes Explored'])
          analyzerObjectAStarMan.append(analyseAStarM)

       #nodesExpAStar=[]
       #nodesExpDFS.append(AStar(Matrix, startX, startY ,n-1,n-1,grid,n,size,p,"Euclidean").solve().to_dict()['Nodes Explored'])
       #rint("ASTAR MANHA")
       #analyzerObjectDFS.append(AStar(Matrix, startX, startY ,n-1,n-1,grid,n,size,p,"Manhatten").solve().to_dict())
       #
       #grid.getMouse()
       #grid.close()
       #grid1.getMouse()
       #grid1.close()
       #grid2.getMouse()
       #grid2.close()
       #grid3.getMouse()
       #grid3.close()
#dfsgrid.close()    grid1.close()
dfs  = pd.DataFrame(analyzerObjectDFS)
bfs  = pd.DataFrame(analyzerObjectBFS)
dfsAStar=pd.DataFrame(analyzerObjectAStar)
dfsAStarMan=pd.DataFrame(analyzerObjectAStarMan)
print("***** Plots ******",dfs['Probability'])
print("***** Plots DFS C Eucledian ******",dfs['Shortest Path'])
print("***** Plots BFS C Eucledian ******",bfs['Nodes Explored'])
print("***** Plots AStar Eucledian ******",dfsAStar['Nodes Explored'])
print("***** Plots A Manhattan ******",dfsAStarMan['Nodes Explored'])

x=np.array(plist)
y=[]
a=x.reshape((len(x),))

y.append(dfs['Nodes Explored'])
y.append(bfs['Nodes Explored'])
y.append(dfsAStar['Nodes Explored'])
y.append(dfsAStarMan['Nodes Explored'])
labels = ['DFS','BFS','AStar Euclidean', 'AStar Manhattan']
print("****X****",np.shape(x))
print("****Y****",np.shape(y))
import matplotlib.pyplot as plt
for y_arr, label in zip(y, labels):
    plt.plot(a, y_arr, label=label)

plt.legend()
plt.show()
#dfs.plot('Probability','Shortest Path')
#print(dfs.groupby('Algo'))
print("***** Plots ******",dfs['Nodes Explored'])
print("***** Plots ******",dfsAStar['Nodes Explored'])

# plt.plot(dfs['Probability'], dfs['Nodes Explored'],dfs['Probability'],dfsAStar['Nodes Explored'])
# plt.show()





















#grid.getMouse()
#grid.close()
#BFS(Matrix,startX,startY,n-1,n-1,grid,n,size).solve()
#AStar(Matrix,startX,startY,n-1,n-1,grid,n,size,"Manhatten").solve()
#Utility.getAlgo("DFS",Matrix,startY,startY,n,grid,size)


#GeneticAlgorithm.performGeneticAlgorithm("DFS", Matrix,startX,startY,grid,size)










