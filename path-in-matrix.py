def existe_caminho(start, end, matrix):
    rows = len(matrix)
    if rows == 0:
        return "Labirinto vazio"
    cols = len(matrix[0])

    sr, sc = start[0], start[1]
    er, ec = end[0], end[1]

    if not (0 <= sr < rows and 0 <= sc < cols):
        return "Posição inicial fora do labirinto"
    if not (0 <= er < rows and 0 <= ec < cols):
        return "Posição final fora do labirinto"
    if matrix[sr][sc] == 1:
        return "Posição inicial é uma barreira"
    if matrix[er][ec] == 1:
        return "Posição final é uma barreira"

    q = []
    q.append([sr, sc])
    
    visited = []
    for _ in range(rows):
        visited.append([False] * cols)
    
    visited[sr][sc] = True
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    while len(q) > 0:
        current_pos = q.pop(0)
        r = current_pos[0]
        c = current_pos[1]

        if r == er and c == ec:
            return "Sim, existe um caminho" 

        for direction in directions:
            dr = direction[0]
            dc = direction[1]
            
            nr = r + dr
            nc = c + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 0 and not visited[nr][nc]):
                visited[nr][nc] = True
                q.append([nr, nc])
    return "O caminho não existe"


matrix = [
  [ 0, 1, 1, 0, 0 ],
  [ 0, 0, 0, 0, 0 ],
  [ 0, 1, 1, 1, 0 ],
  [ 1, 1, 0, 1, 1 ],
  [ 0, 0, 0, 0, 0 ]
]

x1, y1 = 0, 0
x2, y2 = 2, 4
response = existe_caminho([x1, y1], [x2, y2], matrix)
print(f"Caminho de [{x1},{y1}] para [{x2},{y2}]: {response}")

x1_fail, y1_fail = 4, 0
response_fail = existe_caminho([x1_fail, y1_fail], [x2, y2], matrix)
print(f"Caminho de [{x1_fail},{y1_fail}] para [{x2},{y2}]: {response_fail}")

x1_wall, y1_wall = 0, 1
response_wall = existe_caminho([x1_wall, y1_wall], [x2, y2], matrix)
print(f"Caminho de [{x1_wall},{y1_wall}] para [{x2},{y2}]: {response_wall}")