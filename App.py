from Edge import Edge
from Node import Node
from Route import Route

node1= Node("A")
node2= Node("B")
node3= Node("C")
node4= Node("D")

edge1 = Edge(1,node1,node2)
edge2 = Edge(1,node2,node3)
edge3 = Edge(1,node3,node4)
edge4 = Edge(4,node3,node2)
edge5 = Edge(2,node1,node4)


node1.adjList.append(edge1)
node1.adjList.append(edge2)
node2.adjList.append(edge3)
node3.adjList.append(edge4)
node3.adjList.append(edge2)

vertexList=[node1,node2,node3,node4]
edgeList=[edge1,edge2,edge3,edge4]

route = Route()
route.calcShortestPath(vertexList,edgeList,node2)
route.getShortestpathTo(node1)



