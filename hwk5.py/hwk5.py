def median_of_medians(list_l: list[int], k:int) -> int|None:
    """
    Returns the kth smallest element in an array, starting from 0th

    @param list_l: (list) the input array
    @param k: (int) the rank to be searched for
    @return pivot: (int) the element at rank, k, or None if it k doesn't exist

    >>> median_of_medians([10, 7, 2, 4, 9, 8, 5, 11, 1], 6)
    9
    """
    # return None if k is not a valid index or if list is empty
    if list_l == [] or k > len(list_l):
        return None
    # create sublists of size 5
    list_of_chunks:list[list[int]] = []
    for i in range(0, len(list_l), 5):
        list_of_chunks.append(list_l[i:i+5])
    # finds the median of each chunk
    medians:list[int] = []
    for chunk in list_of_chunks:
        chunk.sort()
        medians.append(chunk[(len(chunk)//2)])
    # find the median of the chunks' medians
    if len(medians) <= 5:
        pivot:int = sorted(medians)[(len(medians)//2)]
    else:
        pivot:int = median_of_medians(medians, len(medians)//2) #type: ignore
    # order the elements relative to the pivot, with elements less than pivot on the left and ones greater on the right
    left:list[int] = []
    right:list[int] = []
    for element in list_l:
        if element < pivot: left.append(element)
        elif element > pivot: right.append(element)
    # recurse through the left or right sublist to find kth element if current pivot != kth element, else return pivot
    position:int = len(left)
    if k < position:
        return median_of_medians(left, k)
    elif k > position:
        return median_of_medians(right, k-position-1)
    else:
        return pivot



    


sample_array:list[int] = [10, 7, 2, 4, 9, 8, 5, 11, 1]
array1:list[int] = [2, 4, 9]
array2:list[int] = [2, 4, 9, 454, 89, 0, 78, 72, 10000, 567, 29, 79]
array3:list[int] = [1,2,3,4,5,6]
array4:list[int] = [6,5,4,3,2,1]
array5:list[int] = []

print(median_of_medians(sample_array, 6)) # 9
print(median_of_medians(array1, 0)) # 2
print(median_of_medians(array2, 6)) # 78
print(median_of_medians(array3, len(array3)//2)) # 4
print(median_of_medians(array4, len(array4)-1)) # 6
