def is_valid_move(x, y, N, matrix, visited):
    return 0 <= x < N and 0 <= y < N and matrix[x][y] == 1 and not visited[x][y]

def find_paths(x, y, N, matrix, visited, path, paths):
    if x == N - 1 and y == N - 1:
        paths.append(''.join(path))
        return
    
    moves = ['U', 'D', 'L', 'R']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if is_valid_move(new_x, new_y, N, matrix, visited):
            visited[new_x][new_y] = True
            path.append(moves[i])
            find_paths(new_x, new_y, N, matrix, visited, path, paths)
            path.pop()
            visited[new_x][new_y] = False

def returnPath(N, matrix):
    if matrix[0][0] == 0 or matrix[N - 1][N - 1] == 0:
        return -1
    visited = [[False for _ in range(N)] for _ in range(N)]
    paths = []
    
    visited[0][0] = True
    find_paths(0, 0, N, matrix, visited, [], paths)

    if not paths:
        return [-1]

    return sorted(paths)

# Test examples
matrix1 = [[1, 0, 0, 0],
           [1, 1, 0, 1], 
           [1, 1, 0, 0],
           [0, 1, 1, 1]]
N1 = 4
print(returnPath(N1, matrix1))

matrix2 = [[1, 0],
           [1, 0]]
N2 = 2
print(returnPath(N2, matrix2))
