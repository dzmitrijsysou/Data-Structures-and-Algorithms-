"""Return A list such that for all j A[j] equal average of S[0],S[1]...S[j]"""

def preffix_average1(S):
    #O(n^2) run time
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total/(j + 1)
    return A

def preffix_average2(S):
    #O(N^2) run time
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:(j+1)])/(j + 1)
    return A

def preffix_average3(S):
    #O(N) run time
    n = len(S)
    A = [0]* n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A

S = [10, 100, 1000, 100000]
print(preffix_average1(S))
print(preffix_average2(S))
print(preffix_average3(S))
