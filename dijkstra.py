#Uses python3

import sys
import queue


VERTEX = 0
WEIGHT = 1
def add_edge(graph, vert1, vert2, weight):
    weighted_edge = [vert2, weight]
    if vert1 in graph:
        graph[vert1].append(weighted_edge)
    else:
        graph[vert1] = weighted_edge


def distance(adj, cost, s, t):
    #write your code here
    return -1


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}
    for _ in range(m):
        vert1, vert2, weight = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2, weight)

    start, end = map(int, sys.stdin.readline().split())
    print(distance(graph, cost, s, t))
