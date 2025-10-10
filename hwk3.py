# Name:  - Olohi Goodness John
# Peers:  - Sanjana Yasna, Isabelle Wang, TAs (not sure if they count but Maggie and Molly)
# References:  - URL of resources used <br>
i: list[int]
j: int

### Didn't add docstrings for these because of the "DO NOT EDIT" command
### DO NOT EDIT ###
def new_array(size: int):
    L = [0] * size
    return L

def printGrid(grid:list[list[str]]) -> None:
    for i in grid:
        for j in i:
            print(j, end=" ")
        print()
### END OF DO NOT EDIT BLOCK ###


def slice(arr:list[int] | list[tuple[int, int]], start: int, exclusive_end:int) -> list[int] | list[tuple[int, int]]:
    """ 
    Returns a subarray of the input array, bounded by indices start and exclusive end

    Keyword arguments:
   :param arr: (list) the input array to the function
   :param start: (int) the starting index of the subarray to be created
   :param exclusive end: (int) the index the subarray stops before
   : return copy_array: (list) the subarray created from the input array

    >>> slice([1,3,2,5,7], 1, 3)
    [3, 2]
    """

    index:int = 0

    copy_array:list[tuple[int, int]] | list[int] = new_array(exclusive_end - start)
    while start < exclusive_end and start < len(arr):
        copy_array[index] = arr[start]
        index += 1
        start += 1

    return copy_array
# Question for next homework: can we initialize an array class and create functions for the class there



# Problem 1: SQUARES
def squares(grid:list[list[str]]) -> None:
    """ 
    Prints the total number of white cell regions and their sizes (number of cells)

    Keyword arguments:
    :param grid: (list(list)) a 2D-list containing chars 'b' and 'w' to represent black and white cells

    
    grid = [['b', 'w'],
            ['w', 'b']]
    >>> squares(grid)
    "The white areas in the grid have the following number of cells: 1, 1,"
    "In total, there are 2 areas of white cells"   
    """

    count_areas:int = 0

    # counts the number of areas
    print(f"The white areas in the grid have the following number of cells:", end = " ")

    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == 'w':
                count_areas += 1
                print(f"{squareHelper(grid, row, col)}", end = ", ")
    
    print(f"\nIn total, there are {count_areas} areas of white cells")

def squareHelper(grid:list[list[str]], row:int, col:int) -> int:
    """ 
    Helper function: Returns the number of white cells in a white-cell region

    Keyword arguments:
    :param grid: (list(list)) the input parent 2D-list
    :param row: (int) index of the inner array containing the white region
    :param col: (nt) index of the first white cell found within the inner array
    :return: (int) the number of white cells in the white region
    
    grid = [['b', 'b', 'b', 'b'],
            ['b', 'b', 'w', 'b'],
            ['b', 'w', 'b', 'b'],
            ['b', 'b', 'b', 'b']]
    >>> squareHelper(grid, 1, 2)
    1
    """

    if grid[row][col] != 'w':
        return 0
    
    grid[row][col] = 'x'
    up = squareHelper(grid, row-1, col)
    down = squareHelper(grid, row+1, col)
    left = squareHelper(grid, row, col-1)
    right = squareHelper(grid, row, col+1)

    return 1 + up + down + left + right
            

# Problem 2: INVERSIONS
def inversions(arr:list[int]) -> int:
    """ 
    Returns the number of inversions in an array and prints it out

    Keyword arguments:
    :param arr: (list(int)) an input array of ints
    :return answer: (int) the number of inversions in the input array

    >>> inversions([1,3,5,2,4,6])
    3
    "There are 3 inversions in [1, 3, 5, 2, 6]"
    """

    print(f"The inversions are: ", end = " ")
    result_list: list[int] # type: ignore
    answer: int
    result_list, answer = invert(arr) # type: ignore
    print(f"\nThere are {answer} inversions in {arr}.")
    return answer

def invert(arr:list[int]) -> tuple[list[int], int]:
    """ 
    Helper function: Divides a list and uses the invertChecker function to return a remerged list with the number of inversions

    Keyword arguments:
    :param arr: (list(int)) an input array of ints
    :return result_list, answer: (list), (int) the remerged list and the number of inversions

    >>> invert([1,3,5,2,4,6])
    [1, 3, 5, 2, 4, 6], 3
    """

    answer:int
    left_list: list[int]
    right_list: list[int]
    answer_left: int
    answer_right: int
    answer = 0
    result_list: list[int]
    invert_count: int

    if len(arr) < 2:
        return arr, 0
    mid = len(arr) // 2
    left_list, answer_left = invert(slice(arr, 0, mid))
    right_list, answer_right = invert(slice(arr, mid, len(arr)))
    answer += answer_left + answer_right
    result_list, invert_count = invertChecker(left_list, right_list)
    answer += invert_count
    return result_list, answer

def invertChecker(arr1:list[int], arr2:list[int]) -> tuple[list[int], int]:
    """ 
    Helper function: Merges two lists and counts the number of inversions across both lists


    Keyword arguments:
    :param arr1: (list) an input array of ints
    :param arr2: (list) an input array of ints
    :return merged, invert_count: (list), (int) merged list, number of inversions

    >>> invertChecker([1,3,5], [2,4,6])
    [1, 3, 5, 2, 4, 6], 3
    """

    merged:list[int] = new_array(len(arr1) + len(arr2))
    index = 0
    invert_count = 0
    itr1, itr2 = 0, 0

    while itr1 < len(arr1) and itr2 < len(arr2):
        if arr2[itr2] < arr1[itr1]:   
            invert_count += len(arr1)-itr1
            print_ptr:int = itr1
            while print_ptr < len(arr1):
                print(f"{arr2[itr2]} and {arr1[print_ptr]}", end = "; ")
                print_ptr+=1
            merged[index] = arr2[itr2]
            itr2 += 1
        else:
            merged[index] = arr1[itr1]
            itr1 += 1

        index += 1
    
    while itr1 < len(arr1):
        merged[index] = arr1[itr1]
        index += 1
        itr1 += 1

    while itr2 < len(arr2):
        merged[index] = arr2[itr2]
        index += 1
        itr2 += 1

    return merged, invert_count

# Problem 3: POINTS
"""Great job, Olohi-- next step: Find a way to avoid the duplicates. DOn't worry too much about it tho. Focus on providing new tests in your main function and putting in docstrings in prep for submission
pass"""


def points(point_list:list[tuple[float, float]]) -> None:
    """
    Prints the two closest points (or set of two closest points) and their distance apart
    
    Keyword arguments:
    :param point_list: (list(tuple)) a list of tuples representing points in the 2D plane

    >>> points((-2,2),(-2,0),(0,0),(1,1),(3,3),(4,0),(5,2))
    The pair(s) with the minimum distance, 1.4142135623730951, apart are:
    [(0, 0), (1,1)],
    """

    # check if point_list is less than 2,return None if so
    if len(point_list) < 2:
        return None
    # sort the points based on x, and pass that to the pointsHelper function
    sorted_points: list[tuple[float, float]] = mergeSortPoints(point_list)
    min_points: list[tuple[float, float]]
    min_distance: float
    min_points, min_distance = pointsHelper(sorted_points)
    print(f"The pair(s) with the minimum distance, {min_distance}, apart are:")
    # print the set of points closest together
    for i in range(0, len(min_points), 2):
        if min_points[i][0] == float('inf'):
            continue
        print(f"{[min_points[i], min_points[i+1]]}", end = ", ")
    print()
    


# Return the two closest points (or set of two closest points)
# Breaks the resulting list into two until list <= 3 elems and then bruteforce euclid calculation
def pointsHelper(sorted_points: list[tuple[float, float]]) -> tuple[list[tuple[float, float]], float]:
    """
    Helper function: Returns the two closest points (or set of two closest points) and their distance apart

    Keyword arguments:
    :param sorted_points: (list(tuple)) a list of tuples representing points in the 2D plane, sorted by x-coordinate
    :return min_points, minimum: (list(tuple)), (float) the set of closest points and their distance apart

    >>> pointsHelper([(-2,2),(-2,0),(0,0),(1,1),(3,3),(4,0),(5,2)])
    [(0,0), (1,1)], 1.4142135623730951
    """

    # base case 1
    # if len(list) <= 1: return the list and float('inf')
    if len(sorted_points) <= 1:
        return sorted_points, float('inf')
    
    # initializes minimum distance tracker, minimum; min_points and mp_index to store the points with min distances
    minimum: float = float('inf')
    maximum_closest_points:int = len(sorted_points) * (len(sorted_points)-1) # maximum number of connections/edges in a graph with n vertices = n(n-1)/2
    min_points: list[tuple[float, float]] = [(float('inf'), float('inf'))] * maximum_closest_points
    mp_index:int = 0
    min_points[mp_index] = sorted_points[0]
    
    # base case2
    # if len(list) <= 3: calculate euclid between all point pairs and return closest points and their distance
    if len(sorted_points) <= 3:
        for i in range(len(sorted_points)):
            for j in range(i+1, len(sorted_points)):
                distance = euclid(sorted_points[i], sorted_points[j])
                if distance < minimum:
                    minimum = distance
                    min_points[mp_index] = sorted_points[i]
                    mp_index += 1
                    min_points[mp_index] = sorted_points[j]
                    mp_index += 1
        return min_points, minimum

    # steps in preparation for recursive step
    # calculate and store the mid index and assign a var mid_points to the elem at mid index
    mid_index = len(sorted_points) // 2
    mid_point:tuple[float, float] = sorted_points[mid_index]

    # recursive case
    left_points: list[tuple[float, float]]
    right_points: list[tuple[float, float]]
    left_distance: float
    right_distance: float
    # get closest points and distance for the left and right parts of the list
    left_points, left_distance = pointsHelper(slice(sorted_points, 0, mid_index+1))
    right_points, right_distance = pointsHelper(slice(sorted_points, mid_index, len(sorted_points)))

    # compare distances from both recursive calls and store the appropriate min_points, minimum
    if left_distance < right_distance: # break to two separate statements
        minimum = left_distance
        # add closest points from left call to the list tracker, min_points
        for i in range(len(left_points)):
            min_points[mp_index] = left_points[i]
            mp_index += 1
    elif right_distance < left_distance:
        minimum = right_distance
        # add closest points from right call to the list tracker, min_points
        for i in range(len(right_points)):
            min_points[mp_index] = right_points[i]
            mp_index += 1
    else: # distances are equal
        minimum = left_distance
        # add closest points from both calls to the list tracker, min_points
        for i in range(len(left_points)):
            min_points[mp_index] = left_points[i]
            mp_index += 1
        for i in range(len(right_points)):
            min_points[mp_index] = right_points[i]
            mp_index += 1

    # move left from the mid_point and check for elements within x distance mid_x - minimum
    itr:int = mid_index-1
    count:int = 0
    # have a pointer iterate through from before and after mid_point to find all elements d/2 distance from the mid_point on both sides
    # count the number of ints within the range to know the size of the array to store the points in
    while itr >= 0 and mid_point[0]-minimum < sorted_points[itr][0]:
        count += 1
        itr -= 1
    itr = mid_index+1
    print(f"current elem, {sorted_points[itr][0]} <= {mid_point[0]+minimum}")
    print(f"mid_x = {mid_point[0]} and hor distance = {minimum}")
    while itr < len(sorted_points) and sorted_points[itr][0] <= mid_point[0]+minimum:
        count += 1
        itr += 1
    print(f"count is {count}")
    # create a new array of size count+1, with +1 accounting for the midpoint which wasn't counted
    across_mid_array:list[tuple[float, float]] = [(0, 0)] * (count+1)
    index:int = 0

    itr = mid_index-1
    # repeat the step, but this time, storing them in across_mid_array
    while itr >= 0 and mid_point[0]-minimum < sorted_points[itr][0]:
        across_mid_array[index] = sorted_points[itr]
        itr -= 1
        index += 1
    itr = mid_index+1
    print(f"index to add to is {index}")
    while itr < len(sorted_points) and sorted_points[itr][0] <= mid_point[0]+minimum:
        across_mid_array[index] = sorted_points[itr]
        itr += 1
        index += 1
    # across_mid_array[index] = sorted_points[mid_index]


    # print(f"the mid array is {across_mid_array}")
    # perform brute force euclid on elements within the range, ie elements in across_mid_array
    for i in range(len(across_mid_array)):
        for j in range(i+1, len(across_mid_array)):
            distance = euclid(across_mid_array[i], across_mid_array[j])
            print(f"distance is {distance}")
            # update as necessary
            if distance == minimum:
                min_points[mp_index] = across_mid_array[i]
                mp_index += 1
                min_points[mp_index] = across_mid_array[j]
                mp_index += 1
                print(f"min_points is {min_points}")
            elif distance < minimum and distance != 0:
                minimum = distance
                maximum_closest_points:int = len(sorted_points) * (len(sorted_points)-1) # maximum number of connections/edges in a graph with n vertices = n(n-1)/2
                min_points: list[tuple[float, float]] = [(float('inf'), float('inf'))] * maximum_closest_points
                mp_index:int = 0
                min_points[0] = across_mid_array[i]
                min_points[1] = across_mid_array[j]
                mp_index = 2

    # return min_points, minimum
    return min_points, minimum


def mergeSortPoints(point_list:list[tuple[float, float]]) -> list[tuple[float, float]]:
  """
  Sorts a list of points (tuples) based on their x-coordinates
  
  Keyword arguments:
  :param point_list: (list(tuple)) a list of tuples representing points in the 2D plane
  :return: (list(tuple)) the sorted list of points

  >>> mergeSortPoints([(-2,2), (0,0), (-2,0),(3,3),(1,1),(5,2),(4,0)])
  [(-2, 2), (-2, 0), (0, 0), (1, 1), (3, 3), (4, 0), (5, 2)]
  """
  # Return a sorted list with the same elements as <lst>
  # Base case
  if len(point_list) < 2:
    return point_list
  # Divide the list into two parts, and sort them recursively.
  mid = len(point_list) // 2
  left_sorted = mergeSortPoints(slice(point_list, 0, mid)) # type: ignore
  right_sorted = mergeSortPoints(slice(point_list, mid, len(point_list))) # type: ignore
  # Merge the two sorted halves. Need a helper here!
  return mergeHelper(left_sorted, right_sorted)



def mergeHelper(lst1: list[tuple[float, float]], lst2: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """
    Helper function: Merges two lists of points (tuples) based on their x-coordinates

    Keyword arguments:
    :param lst1: (list(tuple)) a list of tuples representing points in the 2D plane
    :param lst2: (list(tuple)) a list of tuples representing points in the 2D plane
    :return: (list(tuple)) the merged list of points

    >>> mergeHelper([(-2,2), (0,0), (-2,0)], [(3,3),(1,1),(5,2),(4,0)])
    [(-2, 2), (-2, 0), (0, 0), (1, 1), (3, 3), (4, 0), (5, 2)]
    """ 
    itr1 = 0
    itr2 = 0
    index = 0
    merged:list[tuple[float, float]] = [(0, 0)] * (len(lst1) + len(lst2))

    while itr1 < len(lst1) and itr2 < len(lst2):
        if lst1[itr1][0] <= lst2[itr2][0]:
            merged[index] = lst1[itr1]
            itr1 += 1
        else:
            merged[index] = lst2[itr2]
            itr2 += 1
        index += 1

    while itr1 < len(lst1):
        merged[index] = lst1[itr1]
        itr1 += 1
        index += 1

    while itr2 < len(lst2):
        merged[index] = lst2[itr2]
        itr2 += 1
        index += 1

    return merged


def euclid(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    """
    Returns the Euclidean distance between two points in the 2D plane

    Keyword arguments:
    :param point1: (tuple) a tuple representing a point in the 2D plane
    :param point2: (tuple) a tuple representing a point in the 2D plane
    :return: (float) the Euclidean distance between the two points

    >>> euclid((0,0), (1,1))
    1.4142135623730951
    """
    return ((point1[0] - point2[0])**2 + (point1[1]-point2[0])**2)**0.5
  
    


def main(): # Test your code here.
    # example_grid = [["b","b","b","b","b","b","b","b","b","b"],
    #     ["b","w","b","b","w","w","b","w","w","b"],
    #     ["b","b","b","b","b","w","b","w","w","b"],
    #     ["b","w","w","w","b","b","w","w","w","b"],
    #     ["b","w","b","w","b","w","w","b","b","b"],
    #     ["b","w","b","w","w","w","b","w","b","b"],
    #     ["b","w","b","b","b","b","w","w","w","b"],
    #     ["b","w","b","w","b","b","w","w","w","b"],
    #     ["b","w","b","w","b","b","w","w","w","b"],
    #     ["b","b","b","b","b","b","b","b","b","b"]]
    # printGrid(example_grid)
    # squares(example_grid)
    
    # example_array = [1,3,5,2,4,6]
    # inversions(example_array)
    
    example_points = [(-2,2),(-2,0),(0,0),(1,1),(3,3),(4,0),(5,2)]
    points(example_points)

    testMerge:list[tuple[float, float]] = [(3, 3), (-2, 0), (1, 1), (-2, 2), (0, 0), (-1, -1)]
    points(testMerge)
    

if __name__ == "__main__":
    main()


