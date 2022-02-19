def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a list"""

    # low indicie = 0
    # high indicie = len(data)
    if low > high:
        return False
    else:
        middle = (low + high)//2
        if target == data[middle]:
            return middle
        elif target < data[middle]:
            return binary_search(data, target, low, middle - 1)
        else:
            return binary_search(data, target, middle + 1, high)

if __name__ == "__main__":
    data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    print("The item found at location: {}".format(binary_search(data, 22, 0, 15)))