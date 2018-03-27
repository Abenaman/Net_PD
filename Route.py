class Route(object):
    HAS_CYCLE = False
    def calcShortestPath(self,vertexList,edgeList,initialVertex):
        initialVertex.minDistance=0
        for i in range(0,len(vertexList)-1):
            for edge in edgeList:
                u = edge.initialVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight
                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecesor = u
        
        for edge in edgeList:
           if self.hasCycle(edge):
                print("Negative cycle detected...")
                self.HAS_CYCLE = True
                return
    def hasCycle(self,edge):
        if (edge.initialVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
            return True
        else:
            return False
    def getShortestpathTo(self, tergetVertex):
        print("Shortest path to targetvertex: ", tergetVertex.minDistance)
        node = tergetVertex
        while node is not None:
            print("%s -> "% node.name)
            node = node.predecesor

                
        