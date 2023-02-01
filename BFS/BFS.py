graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : [],
    '8' : []
}

visited = []
queue = []

def bfs(graph,node):

    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m , end=" ")

        for neighbor in graph[m]:
            if neighbor  not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


print("Following is the Breadth First Search")                

bfs = bfs(graph,'5')
print(bfs)