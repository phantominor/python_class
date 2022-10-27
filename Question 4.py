'''
A group of n prisoners (0 ~ n-1) stand in a circle in order awaiting execution. Starting from position 0, the executioner kills every kth person until one person remains standing, who is then granted freedom. Create a function who_goes_free(n,k) that takes 2 arguments — the number of people to be executed n, and the step size k, and returns the original position (index) of the person who survives. Assume that 20 > n > k > 0.

For example, if we run who_goes_free(9, 2), then

Prisoners = [0, 1, 2, 3, 4, 5, 6, 7, 8] (Executed people replaced by a dash - for illustration purposes.)
1st round of execution = [0, -, 2, -, 4, -, 6, -, 8] -> [0, 2, 4, 6, 8] (start from 0; step size is 2)
2nd round = [-, 2, -, 6, -] -> [2, 6] (0 is killed in this round because it's beside 8 who was skipped over.)
3rd round = [2, -]
Thus, the function returns 2.
Another example, if we run who_goes_free(9, 3), then

[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, -, 3, 4, -, 6, 7, -] -> [0, 1, 3, 4, 6, 7]
[0, 1, -, 4, 6, -] -> [0, 1, 4, 6]
[0, 1, -, 6] -> [0, 1, 6]
[0, -, 6] -> [0, 6]
[0, -] -> [0]
return 0
Examples:

>>> print(who_goes_free(9, 2))
2

>>> print(who_goes_free(9, 3))
0

>>> print(who_goes_free(12, 3))
9
'''