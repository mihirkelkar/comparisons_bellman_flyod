#!/usr/bin/python

import sys
import time
import random
import bellman_ford
import dijkstra

def generate_graph(no_of_vertices):
    G =[[0 for i in range(no_of_vertices)] for j in range(no_of_vertices)]

    for i in range(no_of_vertices):
        no_of_edges = random.randint(1, 20)
        for j in range(no_of_edges):
            destination = random.randint(i, no_of_vertices - 1)
            if not i == destination:
                weight =  random.randint(1, 25)
                G[i][destination] = weight
                G[destination][i] = weight

    f = open('input_graph.txt', 'w')
    f.write(str(no_of_vertices) + '\n')
    for i in range(no_of_vertices):
    	for j in range(no_of_vertices):
	    f.write(str(G[i][j]) + ' ')
        f.write('\n')

    f.close()


def main():
    f1 = open('timeplot_bellman.csv', 'w')
    f2 = open('timeplot_dijkstra.csv', 'w')

    for i in [4, 6, 10]:
    	print "------------------------"
    	print "No of nodes: $", i
        generate_graph(i)
        bellman_start_time = time.time()
        bellman_ford.main()
        f1.write(str(i) + ',' + str(time.time() - bellman_start_time) + '\n')
        dijkstra_start_time = time.time()
        dijkstra.main()
        f2.write(str(i) + ',' + str(time.time() - dijkstra_start_time) + '\n')

    f1.close()
    f2.close()

main()
