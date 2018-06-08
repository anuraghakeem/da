graph={1: [2,3], 2: [1,3,4,5], 3: [1,2,6,7], 4: [2,5,8,9], 5: [4,9], 6: [3,7], 7: [3,6], 8:[4,9], 9:[4,5,10], 10:[9]}
def bfs(graph, start):
    explored = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in explored:
            print (node)
            explored.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored

bfs(graph,1)
