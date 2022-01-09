# a simple representation of graph using adjacency
# matrix


# class Graph:

#     def __init__(self, numvertex):
#         self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
#         self.numvertex = numvertex
#         self.vertices = {}
#         self.verticeslist = [0]*numvertex

#     def set_vertex(self, vtx, id):
#         if 0 <= vtx <= self.numvertex:
#             self.vertices[id] = vtx
#             self.verticeslist[vtx] = id 

#     def set_edge(self, frm, to, cost=0):
#         frm = self.vertices[frm]
#         to = self.vertices[to]  
#         self.adjMatrix[frm][to] = cost

#         # for directed graph do not add this 
#         self.adjMatrix[to][frm] = cost 

#     def get_vertex(self):
#         return self.verticeslist

#     def get_edges(self):
#         edges = []
#         for i in range(self.numvertex):
#             for j in range(self.numvertex):
#                 if(self.adjMatrix[i][j]!=-1):
#                     edges.append((self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]))
#         return edges

#     def get_matrix(self):
#         return self.adjMatrix

# G = Graph(6)
# G.set_vertex(0, 'a')
# G.set_vertex(1, 'b')
# G.set_vertex(2, 'c')
# G.set_vertex(3, 'd')
# G.set_vertex(4, 'e')
# G.set_vertex(5, 'f')
# G.set_edge('a', 'e', 10)
# G.set_edge('a', 'c', 20)
# G.set_edge('c', 'b', 30)
# G.set_edge('b', 'e', 40)
# G.set_edge('e', 'd', 50)
# G.set_edge('f', 'e', 60)

# print('Vertices of Graph')
# print(G.get_vertex())

# print('\nEdge of Graph')
# print(G.get_edges())

# print('\nAdjacency Matrix of Graph')
# print(G.get_matrix())
 

# a class to represent the adjacency list of the node
# class AdjNode:
    
#     def __init__(self, data):
#         self.vertex = data
#         self.next = None


# # a class to represent a graph. a graph 
# # is the list of the adjacency lists.
# # size of the array will be the no. of the 'V'
# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [None] * self.V

#     # function to add an edge in an undirected graph
#     def add_edge(self, src, dest):

#         # adding the node to the source node
#         node = AdjNode(dest)
#         node.next = self.graph[src]
#         self.graph[src] = node

#         # adding the source node to the destination as
#         # it is the undirected graph 
#         node = AdjNode(src)
#         node.next = self.graph[dest]
#         self.graph[dest] = node

#     # function to print the graph
#     def print_graph(self):
#         for i in range(self.V):
#             print('Adjacency list of vertex {}\n head'.format(i), end='')
#             temp = self.graph[i]
#             while temp:
#                 print(' -> {}'.format(temp.vertex), end='') 
#                 temp = self.graph[i]
#                 while temp:
#                     print(' -> {}'.format(temp.vertex), end='') 
#                     temp = temp.next 
#                 print(' \n')


# # driver program to the above graph class 
# if __name__ == '__main__':
#     V = 5
#     graph = Graph(V)
#     graph.add_edge(0, 1)
#     graph.add_edge(0, 4)
#     graph.add_edge(1, 2)
#     graph.add_edge(1, 3)
#     graph.add_edge(1, 4)
#     graph.add_edge(2, 3)
#     graph.add_edge(3, 4)

#     graph.print_graph()


# python program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# this class represents a directed graph
# using adjacency list representation
# class Graph:

#     # constructor
#     def __init__(self):

#         # default dictionary to store graph 
#         self.graph = defaultdict(list)

#     # function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)

#     def BFS(self, s):

#         # mark all the vertices as not visited
#         visited = [False] * (max(self.graph) + 1)

#         # created a queue for BFS 
#         queue = []

#         # mark the source node as
#         # visited and enqueue it 
#         queue.append(s)
#         visited[s] = True

#         while queue:

#             # Dequeue a vertex from the queue
#             # print it
#             s = queue.pop(0)
#             print(s, end=' ')

#             # get all adjacent vertices of the 
#             # dequeued vertex s. If a adjacent
#             # has not been visited, then mark it 
#             # visited and enqueue it
#             for i in self.graph[s]:
#                 if visited[i] == False:
#                     queue.append(i)
#                     visited[i] = True

# # Driver code

# # create a graph given in 
# # the above diagram
# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

# print('Following is Breadth First Traversal (starting from vertex 2)')
# g.BFS(2)


# python program to print DFS traversal
# from a given graph 
from collections import defaultdict

# this class represents a directed graph using 
# adjacency list representation

class Graph:

    # constructor
    def __init__(self):

        # defualt dictionary to store graph 
        self.graph = defaultdict(list)

    # function to add an edge to graph 
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # a function used by DFS 
    def DFSUtil(self, v, visited):

        # Mark the current node as visited 
        # and print it 
        visited.add(v)
        print(v, end='')

        # recur for all the vertices
        # adjacent to this vertex
        for neighbor in self.graph[v]: 
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    # the function to do DFS traversal. it uses 
    # recursive DFSUtil()
    def DFS(self, v):

        # create a set to store visited vertices
        visited = set()

        # call the recursive helper function 
        # to print DFS traversal
        self.DFSUtil(v, visited)


# Driver code 

# create a graph given 
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print('following is DFS from (starting from vertex 2)')
g.DFS(2)