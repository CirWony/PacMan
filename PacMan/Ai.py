graphBlinky = {'a': {'b': 1, 'e': 2},
               'b': {'a': 1},
               'c': {'d': 1},
               'd': {'c': 1, 'f': 2},
               'e': {'a': 1, 'f': 2, 'j': 3},
               'f': {'d': 1, 'e': 2, 'm': 3},
               'g': {'h': 1, 'k': 2},
               'h': {'g': 1, 'i': 2},
               'i': {'h': 1, 'l': 2},
               'j': {'k': 1, 'p': 2},
               'k': {'j': 1, 'g': 2, 'n': 3},
               'l': {'i': 1, 'm': 2, 'o': 3},
               'm': {'l': 1, 'f': 2, 'q': 3},
               'n': {'k': 1, 'o': 2},
               'o': {'l': 1, 'n': 2},
               'p': {'j': 1, 'u': 2},
               'q': {'m': 1, 'v': 2},
               'r': {'p': 1, 'u': 2, 's': 3},
               's': {'q': 1, 'v': 2, 'r': 3},
               't': {'u': 1, 'x': 2},
               'u': {'t': 1, 'p': 2},
               'v': {'w': 1, 'q': 2},
               'w': {'v': 1, 'y': 2},
               'x': {'t': 1, 'y': 2},
               'y': {'w': 1, 'x': 2}}


def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseen_nodes = graph
    infinity = 9999999
    path = []
    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for childNode, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[min_node]
                predecessor[childNode] = min_node
        unseen_nodes.pop(min_node)

    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        # print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))


dijkstra(graphBlinky, 'a', 'd')
