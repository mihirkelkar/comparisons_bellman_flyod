						# Source Code for Dijkstra's algorithm #
import sys
import memoryusage

def dijkstra(G, no_of_vertices, source, dest):
    distance = [float('Inf') for i in range(no_of_vertices)] #initialize the distance vector, visited list to infinity
    visited = [0 for i in range(no_of_vertices)]
    shortestPath = [1000 for i in range(no_of_vertices)]

    for i in range(0, dest + 1):
        shortestPath[i] = 1000

    visited[source] = 1	# visit the source node
    distance[source] = 0  
    currentNode = source   
    while(currentNode != dest):
        smalldist = float('Inf')
        dc = distance[currentNode]
        for i in range(no_of_vertices):
            if visited[i] == 0 and G[currentNode][i] != 0:
                newdist = dc + G[currentNode][i]
                if(newdist < distance[i]):
                    distance[i] = newdist
                if(distance[i] < smalldist):
                    smalldist = distance[i]
                    k = i
        currentNode = k
        visited[currentNode] = 1
    return distance


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
    dest = no_of_vertices - 1
    distance = dijkstra(G, no_of_vertices, source, dest)


    print "Distance : ",
    print distance[dest]

    f = open('dijkstra_memory.txt', 'a')
    memory = memoryusage.memory_usage()
    f.write(str(memory['rss']) + '\n')
    f.close()
