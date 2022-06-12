def bubble_sort(list):
    """
        Sorts a list of items in ascending order
        runs in a timespace of O(n)
    """
    includes_swap = False
    i, j = 0, 1

    while j < len(list):
        if list[j] < list[i]:
            container = list[i]
            list[i] = list[j]
            list[j] = container
            includes_swap = True
        j+=1
        i+=1
    return bubble_sort(list) if includes_swap else list




    

   
