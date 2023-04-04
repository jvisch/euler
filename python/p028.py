width = 1001

MOVE_RIGHT = 0
MOVE_BOTTOM = 1
MOVE_LEFT = 3
MOVE_TOP = 4


matrix = [ [-1 for i in range(width)] for i in range(width)]

row = col = width // 2
move = MOVE_RIGHT

for cell in range(1, width*width + 1):
    matrix[row][col] = cell
    if move == MOVE_RIGHT:
        if matrix[row+1][col] == -1:
            move = MOVE_BOTTOM
            row += 1
        else:
            col += 1
    elif move == MOVE_BOTTOM:
        if matrix[row][col-1] == -1:
            move = MOVE_LEFT
            col -= 1
        else:
            row +=1
    elif move == MOVE_LEFT:
        if matrix[row-1][col] == -1:
            move = MOVE_TOP
            row -= 1
        else:
            col -= 1
    elif move == MOVE_TOP:
        if matrix[row][col+1] == -1:
            move = MOVE_RIGHT
            col += 1
        else:
            row -= 1


total = 0
row = 0
for col in range(width):
    total += matrix[row][col]
    total += matrix[width - row-1][col]
    row += 1
total -= matrix[width//2][col//2]

print (total)