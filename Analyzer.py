
class Analyzer:
    def __init__(self, matrix,shortestPath,nodesExplored,fringeSize,totalTime,mazeSolved,algo,prob,size):
        self.matrix=matrix
        self.shortestPath = shortestPath
        self.nodesExplored= nodesExplored
        self.fringeSize = fringeSize
        self.totalElapsed = totalTime
        self.isMazeSolved  = mazeSolved
        self.algo = algo
        self.prob = prob
        self.size = size

    def to_dict(self):
        return {
            'Algo':self.algo,
            'Probability':self.prob,
            'Map Size':self.size,
            'Nodes Explored': self.nodesExplored,
            'Fringe Size':self.fringeSize,
            'Time Elapsed(in sec)': self.totalElapsed,
            'Maze Solved':self.isMazeSolved,
            'Shortest Path': self.shortestPath,
        }


