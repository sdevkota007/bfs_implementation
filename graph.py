import test_cases
from collections import defaultdict
import random


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

        # Function to print a BFS of graph

    def generateGraph(self, num_nodes):
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                self.addEdge(i, j)

    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True


        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s)

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            print self.graph[s]
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ =="__main__":
    g= Graph()
    g.generateGraph(5)
    print g.graph
    g.BFS(2)