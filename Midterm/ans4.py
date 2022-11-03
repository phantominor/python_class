def who_goes_free(n,k):
    prisoners = list(range(n))
    while len(prisoners) > 1:
        for i in range(k-1):
            prisoners = prisoners + [prisoners.pop(0)]
        prisoners.pop(0)
    return prisoners.pop()

print(who_goes_free(12,3))