from queue import Queue

def bfs(start, end, graph):
    q = Queue()
    path = {}
    
    if start not in graph:
        return "O caminho não existe"
    
    q.put(start)
    path[start] = None
    found = False

    while not q.empty():
        node = q.get()
        list = graph[node]
        for item in list:
            if item not in path:
                path[item] = node
                q.put(item)
                if item == end:
                    found = True
                    break
        if found:
            break

    if not found:
        return "O caminho não existe"

    response = []
    aux = end
    while aux is not None:
        response.append(aux)
        aux = path[aux]
    response.reverse()
    return response


graph = {
    "A": ["B"],
    "B": ["C", "E"],
    "C": ["D"],
    "D": ["F"],
    "E": ["F"],
    "F": ["D", "E"]
}
response = bfs("A", "F", graph)
print(response)
if response != "O caminho não existe":
    print(len(response))