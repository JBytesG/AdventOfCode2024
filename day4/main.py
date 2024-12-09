f = open("input", "r")
sum = 0
grid = []

for l in f:
    grid.append(l)


def searchAround(row, col, char):
    finds = []
    for r in range(3):
        for c in range(3):
            if len(grid) > row - 1 + r and len(grid[row]) > col - 1 + c and row - 1 + r >= 0 and col - 1 + c >= 0:
                if grid[row - 1 + r][col - 1 + c] == char:
                    finds.append([r - 1,c - 1])
    return finds

print(searchAround(0,0,'M'))

for r in range(len(grid)):
    for c in range(len(grid[r])):
        m = []
        if grid[r][c] == 'X':
            m = searchAround(r ,c, 'M')
        if m != []:
            for find in m:
                if len(grid) > r + 3*find[0] and len(grid[r]) > c + 3*find[1]:
                    if grid[r + 2*find[0]][c + 2*find[1]] == 'A':
                        if grid[r + 3*find[0]][c + 3*find[1]] == 'S':
                            sum += 1

print(sum)