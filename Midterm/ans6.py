def maze_path(maze, goal):
    visited = []
    i = (0,0)
    action = []
    size = len(maze)-1
    while i != goal:
        visited.append(i)
        if i[0] > 0 and maze[i[0]-1][i[1]] == 'O' and (i[0]-1,i[1]) not in visited:
            action.append('N')
            i = (i[0]-1,i[1])
        elif i[1] > 0 and maze[i[0]][i[1]-1] == 'O' and (i[0],i[1]-1) not in visited:
            action.append('W')
            i = (i[0],i[1]-1)
        elif i[0] < size and maze[i[0]+1][i[1]] == 'O' and (i[0]+1,i[1]) not in visited:
            action.append('S')
            i = (i[0]+1,i[1])
        elif i[1] < size and maze[i[0]][i[1]+1] == 'O' and (i[0],i[1]+1) not in visited:
            action.append('E')
            i = (i[0],i[1]+1)
    return ''.join(action)

X='X'
O='O'
maze = [[O,X,X,X,X,X],
        [O,O,O,X,X,X],
        [X,X,O,O,X,X],
        [X,X,X,O,O,X],
        [X,X,X,X,O,X],
        [X,X,X,X,O,O]]
print(maze_path(maze,(5,5)))