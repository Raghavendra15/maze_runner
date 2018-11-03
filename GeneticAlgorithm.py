from Utility import *
from queue import PriorityQueue
import numpy as np
import math as math

class Calculate:
    def __init__(self,matrix, pathLength):
        self.priority = pathLength
        self.matrix = matrix

    def __gt__(self, other):
        return self.priority < other.priority

class GeneticAlgorithm:

    mutation = 1
    repeatProcess = 10
    crossOverPortion = 10
    def __init__(self):
        print("Gautam")
        self.priorityQueue = PriorityQueue()


    def performCrossover(self,listOfMatrix):
        newList = []
        length = len(listOfMatrix)
        n = 0
        if length!=0:
            n = len(listOfMatrix[0])
        firstPortion = math.ceil((GeneticAlgorithm.crossOverPortion*n)/100)
        for i in range(0,length,2):
            first = np.array(listOfMatrix[i])[:,:firstPortion]
            second = np.array(listOfMatrix[i+1])[:,firstPortion:]
            temp = np.concatenate((first,second),axis=1)
            temp[0][0] =  1
            temp[n-1][n-1] = 1
            newList.append(temp)
        return newList

    def storeInQueue(self,list):
        len = len(list)
        for i in range(len):
            self.priorityQueue.put(Calculate(list[i].shortestPath, list[i].matrix))

    def performMutation(self,listOfMatrix):
        matSize = len(listOfMatrix)
        for i in range(matSize):
            n = len(listOfMatrix[i])
            num = math.ceil((GeneticAlgorithm.mutation * n* n) / 100)
            x = np.random.randint(n, size=(num, 2))
            xLen = len(x)
            for j in range(xLen):
                listOfMatrix[i][x[j][0]][x[j][1]] = 1 - listOfMatrix[i][x[j][0]][x[j][1]]
                listOfMatrix[i][0][0] = 1
                listOfMatrix[i][n-1][n-1]=1
            print("Gautam")

    def performGeneticAlgorithm(self,type,matrix,startX,startY,grid,size):
        listOfMatrix = []
        analysisOjbs = []
        for j in range(10):
            listOfMatrix.append(Utility.shuffle(matrix))
            #self.performSelection(listOfMatrix)
        lenNewList = len(listOfMatrix)
        for k in range(lenNewList):
            analysisOjbs.append(Utility.getAlgo(type, listOfMatrix[k], startX, startY, grid, size).solve())
        self.storeInQueue(analysisOjbs)
        listOfMatrix = []

        for i in range(GeneticAlgorithm.repeatProcess):
            for j in range(10):
                listOfMatrix.append(self.priorityQueue.get().matrix)
                # self.performSelection(listOfMatrix)
            newList = self.performCrossover(listOfMatrix) #it should get 5 elements
            self.performMutation(newList)
            lenNewList = len(newList)
            analysisOjbs = []
            for k in range(lenNewList):
                analysisOjbs.append(Utility.getAlgo(type, newList[k], startX, startY, grid, size).solve())
            self.storeInQueue(analysisOjbs)