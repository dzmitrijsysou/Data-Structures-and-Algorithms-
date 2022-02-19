"""Return True if there is no element common to all three lists."""

def disjoint1(A, B, C):
    #O(N^3)
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


def disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b: # Check C only if A and B are matching
                for c in C:
                    if a == c:
                        return False
    return True

A = [11, 21, 3, 4]
B = [12, 22, 5, 6]
C = [13, 23, 3, 5]

print(disjoint1(A, B, C))
print(disjoint2(A, B, C))
