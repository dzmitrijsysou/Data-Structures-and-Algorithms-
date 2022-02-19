def insert_sort(S):
    print("S = {}".format(S))
    for j in range(1, len(S)):
        key = S[j]
        i = j - 1
        while i >= 0 and S[i] > key:
            S[i + 1] = S[i]
            i -= 1
            print("Key = {}, S = {}".format(key, S))
        S[i + 1] = key
    return S




if __name__ == "__main__":
    S = [5,4,3,2,1]
    print("Solution = {}".format(insert_sort(S)))
