def linear_search(list, element):
    """
    Returns the index value of element
    and None if element does not exist in list
    """

    for i in range(0, len(list)):
        if list[i] == element:
            return i

    return None


def verify(index):
    if index:
        print("Element index is: ", index)
    else:
        print("Element does not exist in the list")


numbers_array = [i for i in range(1, 101)]

verify(linear_search(numbers_array, 50))
verify(linear_search(numbers_array, 200))
