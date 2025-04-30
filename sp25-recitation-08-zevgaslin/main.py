from collections import deque
from heapq import heappush, heappop


def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """

    ### TODO
    queue = []
    heappush(queue, (0, 0, source))
    named = {}
    while queue:
        distance_weight, distance_edges, node = heappop(queue)
        if node in named:
            continue
        named[node] = (distance_weight, distance_edges)
        
        for neighbor, weight in graph.get(node, []):
            if neighbor not in named:
                heappush(
                    queue,
                    (distance_weight + weight, distance_edges + 1, neighbor))

    return named


def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """

    ###TODO
    def bfs_pathed(named, queue, parents): 
        if len(queue) == 0:
            return parents
        else:
            current_vertex = queue.popleft()
            for n in graph[current_vertex]:
                if n not in named:
                    named.add(n)  
                    parents[n] = current_vertex
                    queue.append(n)
            return bfs_pathed(named, queue, parents)

    parents = dict()
    queue = deque()
    queue.append(source)
    named = set()
    named.add(source)  
    return bfs_pathed(named, queue, parents)


def get_sample_graph():
    return {'s': {'a', 'b'}, 'a': {'b'}, 'b': {'c'}, 'c': {'a', 'd'}, 'd': {}}


def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    if destination in parents:
        return get_path(parents, parents[destination]) + parents[destination]
    else:
        return ''
