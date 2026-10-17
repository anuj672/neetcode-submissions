class Graph:
    
    def __init__(self):
        self.adjList = {}
        


    def addEdge(self, src: int, dst: int) -> None:

        if src not in self.adjList:
            self.adjList[src] = []

        if dst not in self.adjList:
            self.adjList[dst] = []

        self.adjList[src].append(dst)    

    def removeEdge(self, src: int, dst: int) -> bool:

        if src not in self.adjList or dst not in self.adjList:
            return False

        self.adjList[src].remove(dst) 
        return True 


    def hasPath(self, src: int, dst: int) -> bool:

        visit = set()
        

        def dfs(src, dst, visit):

            if src == dst:
                return True

            visit.add(src)

            for i in self.adjList[src]:
                if i not in visit:
                    if dfs(i, dst, visit):
                        return True    
            return False  

        return dfs(src,dst, visit)      

