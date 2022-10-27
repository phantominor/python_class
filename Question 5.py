'''
Following hw2_4, Dora and Boots got on the helicopter after their exciting adventure. Unfortunately, the helicopter pilot was Swiper !! (a fox, as the following figure shows.) They were dropped from the helicopter by Swiper, and they are on an island now. Luckily, Boots finds a map, which records the connection of 100 islands here (No.1 to No.100), so they decide to explore these islands. The map is a list of tuples (start, end), where 0 <= start < end <= 100, which records the one-way bridge (unidirectional bridge, only from start to end) between two islands. In addition, the map notes that:

They are on Island No.1 now.
For each island j, the bridge (x,j) they can use to reach island j is at most one. (Given j, x is unique for (x,j).)
That is, all the tuples must have a different end (but the start may be the same.) i.e., (2,3) and (2,5) comply with the rule; however, (2,5) and (3,5) do not.
The bridge would collapse after someone passing.
As hw2_4, they will do their best to explore these 100 islands. Since they can not go back after passing a bridge, please help them determine the path so that they can explore the islands as much as possible. In addition, Boots want to know how many bridges will collapse after this adventure. Thus, write a function to tell them. The input is the list of tuples. The output is the total number of the bridge they will pass.

Hint: You do not need to determine the path. Just count the number of bridges they will pass.

Examples:

>>> dora([(1,2),(2,4),(4,5),(5,6),(6,7),(7,8),(8,9),(2,3),(3,14),(14,15)])
7  # Consists of (1,2),(2,4),(4,5),(5,6),(6,7),(7,8),(8,9), and there are 7 tuples, meaning seven bridges.

>>> dora([(1,2),(1,4),(1,5),(5,6),(4,7),(7,8),(2,19),(19,20),(20,23),(23,24)])
5 # 1 --> 2 --> 19 --> 20 --> 23 --> 24. five bridges.
'''