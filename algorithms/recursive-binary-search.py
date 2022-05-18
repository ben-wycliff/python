def recursive_binary_search(list, target):
    """
    Binary search algorithm implementation using recursion
    returns True if elements exists
    Parameters
    ----------
    list: array containing elements
    target: element being sought

    """
    if len(list) == 0:
        return None

    middle_point = len(list) // 2

    if list[middle_point] == target:
        return True
    else:
        if list[middle_point] < target:
            return recursive_binary_search(list[middle_point + 1 :], target)
        else:
            return recursive_binary_search(list[:middle_point], target)

    return None


def verify(list, target):
    if recursive_binary_search(list, target):
        print(f"Found element {target} in list {list}")
    else:
        print(f"Element {target} does not exist in list {list}")


list = [1, 2, 4]

verify(list, 2)
verify(list, 1.5)
verify(list, 1)
