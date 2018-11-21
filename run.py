
import test_cases
from collections import defaultdict
import json
import time
from test_cases import write_to_file




class Graph:
    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.consistency = True
        self.run_time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Function to print a BFS of graph
    def generateGraph(self, num_nodes):
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                self.addEdge(i, j)

    def BFS(self, s, judgements):
        start_time = time.time()
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        starting_node = s
        group_a = [starting_node]
        group_b = []
        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            # print (s)

            if s!= starting_node:
                judgement = judgements['{}-{}'.format(s, starting_node)] if starting_node > s \
                    else judgements['{}-{}'.format(starting_node, s)]  # get_judgement
                if judgement == 's':
                    group_a.append(s)

                elif judgement == 'd':
                    group_b.append(s)

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


        self.run_time = time.time() - start_time
        # print group_a
        # print group_b
        for edge, judgement in judgements.items():
            # print edge, judgement
            u_v = edge.split("-")
            u = u_v[0]
            v = u_v[1]
            if judgement == 's':
                if (int(u) in group_a and int(v) in group_b) or (int(u) in group_b and int(v) in group_a):
                    self.consistency = False
                    break
            if judgement == 'd':
                if (int(u) in group_a and int(v) in group_a) or (int(u) in group_b and int(v) in group_b):
                    self.consistency = False
                    break



def brute_force(judgements, num_samples):
    consistency = True
    group_a = []
    group_b = []

    i = 0
    for species_1 in range(num_samples):
        A = []
        B = []
        if group_a:
            if species_1 in group_a[0]:
                A.append(species_1)
        elif group_b:
            if species_1 in group_b[0]:
                B.append(species_1)
        else:
            A.append(species_1)

        for species_2 in range(species_1 + 1, num_samples):
            judgement = judgements["{}-{}".format(species_1, species_2)]
            if i == 0:
                if judgement == 's':
                    A.append(species_2)
                elif judgement == 'd':
                    B.append(species_2)

            elif i != 0:
                if species_1 in group_a[0]:
                    if judgement == 's':
                        A.append(species_2)
                        if species_2 in group_b[0]:
                            # print "Brute Force Solution: Judgements were inconsistent"
                            consistency = False
                            break
                    elif judgement == 'd':
                        B.append(species_2)
                        if species_2 in group_a[0]:
                            # print "Brute Force Solution: Judgements were inconsistent"
                            consistency = False
                            break

                elif species_1 in group_b[0]:
                    if judgement == 's':
                        B.append(species_2)
                        if species_2 in group_a[0]:
                            # print "Brute Force Solution: Judgements were inconsistent"
                            consistency = False
                            break

                    elif judgement == 'd':
                        A.append(species_2)
                        if species_2 in group_b[0]:
                            # print "Brute Force Solution: Judgements were inconsistent"
                            consistency = False
                            break

        i = +1
        group_a.append(A)
        group_b.append(B)
        if not consistency:
            break

    # print group_a
    # print group_b
    return consistency


def main():
    print "Loading all test samples..."
    with open(test_cases.FILE_NAME) as f:
        data = json.load(f)

    small_sample_size = 10
    large_sample_size = 1000

    print "\n**********Brute Force Solution for first {} samples**********".format(small_sample_size)
    brute_force_solutions = []
    for i, judgements in enumerate(data['samples'][:small_sample_size]):
        num_node = i+2
        consistency = brute_force(judgements, num_node)
        if consistency:
            print "Test case {}: Judgements were consistent.".format(i)
            brute_force_solutions.append(True)
        else:
            print "Test case {}: Judgements were inconsistent.".format(i)
            brute_force_solutions.append(False)


    print "\n**********BFS Solution for first {} samples**********".format(small_sample_size)
    time.sleep(2)
    bfs_solutions = []
    for i, judgements in enumerate(data['samples'][:small_sample_size]):
        num_node = i+2
        g = Graph()
        g.generateGraph(num_node)
        # print g.graph
        # print ("Following is the BFS implementation")
        g.BFS(1, judgements)
        if g.consistency == True:
            print "Test case {}: Judgements were consistent.".format(i)
            bfs_solutions.append(True)
        else:
            print "Test case {}: Judgements were inconsistent.".format(i)
            bfs_solutions.append(False)


    if bfs_solutions == brute_force_solutions:
        print "\nTest cases validated for small n"
    else:
        print "\nTest cases could not validate for small n"
    print "\n**********Implementing algorithm for all generated samples**********".format(large_sample_size)
    time.sleep(2)
    runtime = {"nodes":[],"runtime":[]}
    for i, judgements in enumerate(data['samples']):
        num_node = i+2
        g = Graph()
        g.generateGraph(num_node)

        g.BFS(1, judgements)
        # if g.consistency == True:
        #     print "Judgements were consistent."
        # else:
        #     print "Judgements were inconsistent."

        # print num_node, g.run_time
        runtime["nodes"].append(num_node)
        runtime["runtime"].append(g.run_time)

    write_to_file(json.dumps(runtime, indent=4), "runtime.json")
    print "Done."




if __name__ == '__main__':
    main()
