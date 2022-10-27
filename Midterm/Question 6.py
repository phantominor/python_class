'''
You are lost in a maze. Luckily, you have a map that illustrates the maze as a matrix.

X='X'
O='O'
maze = [[O,X,X,X,X,X],
        [O,O,O,X,X,X],
        [X,X,O,O,X,X],
        [X,X,X,O,O,X],
        [X,X,X,X,O,X],
        [X,X,X,X,O,O]]
The X is equal to the string 'X', which indicates the barrier. In contrast, The O is equal to the string 'O', which indicates the road you can go. Define a function that can help you pass the maze. The inputs are the maze and the coordinate of the goal position. ((0,0) is on the upper left.) Note that the goal position can be anywhere in the maze, and you are initially at (0,0). In addition, you can not leave the maze across the boundary.

The output is the NEWS string sequence that can guide you to pass the maze. ('N' is ↑; 'S' is ↓; 'E' is →; 'W' is ←)

Assume that there is no fork on the road, and there is a single path to the goal.
'''

'''
>>> X='X'
>>> O='O'
>>> maze = [[O,X,X,X,X,X],
...         [O,O,O,X,X,X],
...         [X,X,O,O,X,X],
...         [X,X,X,O,O,X],
...         [X,X,X,X,O,X],
...         [X,X,X,X,O,O]]
>>> print(maze_path(maze,(5,5)))
SEESESESSE # starting from the upper left 'O', you can arrive (5,5) after applying this sequence.
'''