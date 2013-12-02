					# Source code for Bellman-Ford Algorithm #
import pdb
import sys
import memoryusage


# initialize the graph G
def initialize(G, no_of_vertices, source):
    distance = [float('Inf') for i in range(no_of_vertices)]
    predecessor = [-1 for i in range(no_of_vertices)]
    distance[source] = 0
    return distance, predecessor

# perform relaxation on the nodes. 
#This section looks whether we have shorter available paths from one node to the other invloving intermediatery nodes
def relax(G, node, neighbor, distance, predecessor):
    if distance[neighbor] > distance[node] + G[node][neighbor]:
        distance[neighbor] = distance[node] + G[node][neighbor]
        predecessor[neighbor] = node


# main function to calculate the shortest path 
#Iterate trough all vertices except for the first one. Calculate distances and look for shorter relaxed paths
def bellman_ford(G, no_of_vertices, source):
    distance, predecessor = initialize(G, no_of_vertices, source)

    for k in range(no_of_vertices - 1):
        for u in range(no_of_vertices):
            for v in range(no_of_vertices):
                if G[u][v] != 0:
                    relax(G, u, v, distance, predecessor)

    return distance, predecessor


# function to read the graph form the file and store it in adjacency matrix
def load_graph():
    file_ptr = open('input_graph.txt', 'r')

    no_of_vertices = int(file_ptr.readline())
    G = [[0 for i in range(no_of_vertices)] for j in range(no_of_vertices)]

    for i in range(no_of_vertices):
        elements = file_ptr.readline().split()
        for j in range(no_of_vertices):
            G[i][j] = int(elements[j])

    file_ptr.close()
    return G, no_of_vertices


def main():
    source = 0
    G, no_of_vertices = load_graph()
    
    distance, predecessor = bellman_ford(G, no_of_vertices, source)

    print "Distances: "
    for i in range(no_of_vertices):
        print distance[i],

    print "\n\nPredecessors: "
    for i in range(no_of_vertices):
        print predecessor[i],

    f = open('bellman_memory.txt', 'a')
    memory = memoryusage.memory_usage()
    f.write(str(memory['rss']) + '\n')
    f.close()
