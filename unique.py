"""Return true if there are no duplicate elements"""
def unique1(S):
    for i in range(len(S)):
        for k in range(i, len(S)):
            if S[i] == S[k]:
                return False
    return True

def unique2(S):
    #O(NLOGN)
    temp = sorted(S);
    for k in range(0, len(temp)):
        if temp[k] == temp[k + 1]:
            return False
    return True


S = [1, 2, 3, 7, 9, 1]
print(unique1(S))
print(unique2(S))