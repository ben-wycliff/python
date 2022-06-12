def binary_search(list, element):
    """
    Returns index value on element in the list
    and None if element does not exist.
    """

    # marking list bounding indicies
    first = 0
    last = len(list) - 1

    while first <= last:
        # get middle index value
        middle = (first + last) // 2

        if list[middle] == element:
            return middle
        elif middle < element:
            first = middle + 1
        else:
            last = middle - 1

    return None


def verify(index):
    if index:
        print("Element index is: ", index)
    else:
        print("Element does not exist in the list")


numbers_array = [i for i in range(1, 101)]

verify(binary_search(numbers_array, 50))
verify(binary_search(numbers_array, 200))
