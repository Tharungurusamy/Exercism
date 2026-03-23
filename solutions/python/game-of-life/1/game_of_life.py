def tick(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    
    def count_neighbors(r, c):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                count += matrix[nr][nc]
        return count
    
    new_matrix = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            live_neighbors = count_neighbors(i, j)
            
            if matrix[i][j] == 1:
                if live_neighbors in (2, 3):
                    new_matrix[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_matrix[i][j] = 1
    
    return new_matrix