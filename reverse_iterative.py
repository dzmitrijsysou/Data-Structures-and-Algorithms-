def reverse_iterative(S):
    start, stop = 0, len(S)
    while start < stop:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        start, stop = start + 1, stop - 1
    return S


if __name__ == '__main__':
    S = [1,2,3,4,5,6,7,8,9]
    print(reverse_iterative(S))