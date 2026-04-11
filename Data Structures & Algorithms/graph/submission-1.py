class Graph:
    
    def __init__(self):
        self.adj_list = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        # add edge
        self.adj_list[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list:
            return False
        self.adj_list[src].remove(dst)
        return True
    
    def _dfs(self, src, dst, visit):
        if src == dst:
            return True
        visit.add(src)
        for nei in self.adj_list.get(src,[]):
            if nei not in visit:
                if self._dfs(nei, dst, visit):
                    return True
        return False
                


    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        return self._dfs(src, dst, visit)

