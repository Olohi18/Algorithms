# Name:  - your name (and your partners name) <br>
# Peers:  - names of CSC252 students who you consulted or ``N/A'' <br>
# References:  - URL of resources used <br>
from collections import deque
# Question: can a graph neither be undirected nor a DAG?
# Can we use a hshset
# Can we assume every node in teh graph would be a key in the hashmap?
# Assumption: State assumption for keys in dictionary. Keys, which are leaf nodes, are included in dictionary with a value of '[]', an empty list
# Assumption: Start and end nodes passed into findBFS are in the graph, ie no need to check whether a node is or is not a key in the graph

#### DO NOT EDIT - START ####
def POL_helper():
    print("File Imported")
#### DO NOT EDIT - END ####

# Part 1: DAG2UG
def convertDAGToUG(dag_graph:dict[str|int, list[str|int]]) -> dict[str|int, list[str|int]]: 
    # initialize a new hash map            
    ug: dict[str|int, list[str|int]] = {}
    
    # iterate through key,value pairs in dag_graph
    for key in dag_graph:
        value = dag_graph[key]
        # add the key to the new hashmap if not already in it
        if key not in ug:
            ug[key] = value
        else:
            # if in it, simply append its absent values to its value list
            for val in value:
                if isIn(val, ug[key]) is False:
                    ug[key].append(val)

        # iterate through every value in dag_graph[key]
        for val in value:
            # add the value as a key to the new hashmap if not in it already
            if val not in ug:
                ug[val] =[key]
            # if in it, append the key to the value list of ug[val]
            else:
                if isIn(key, ug[val]) is False:
                    ug[val].append(key)

    return ug

def isIn(val:str | int, array:list[str | int]):
    for elem in array:
        if elem == val:
            return True

    return False



# Part 2: BFS            
def findBFSPath(graph:dict[str|int, list[str|int]], start_node:str, end_node:str) -> list[str|int] | None:
    queue:deque[str|int] = deque()
    visited:dict[str|int, str|int] = dict()
    queue.append(start_node)
    while queue:
        popped:str|int = queue.popleft()
        if popped == end_node:
            return path(visited, popped, start_node)
        else:
            for value in graph[popped]:
                if value not in visited:
                    visited[value] = popped
                    queue.append(value)

    return None

def path(visited:dict[str|int, str|int], popped:str|int, start:str|int) -> list[str|int]:
    result:list[str|int] = []
    current:str|int = popped
    while current != start:
        result.append(current)
        current = visited[current]
    result.append(start)
    # reverse the list and return
    left, right = 0, len(result)-1
    while left <= right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    return result


# Part 3: ISCYCLIC
def isCyclic(graph:dict[str|int, list[str|int]]) -> bool:
    # iterate through keys in the graph
    for key in graph:
        # if findPath(key, key) == True, return False
        if isCylicHelper(key, graph) == True:
            return True
    # return True
    return False

def isCylicHelper(key:str|int, graph:dict[str|int, list[str|int]]) ->bool:
    # initialize a queue
    queue:deque[str|int] = deque()
    # initialize a hashset
    hash_set:set[int|str] = set()
    # push all of key's neighbors (graph[key]) onto the queue
    for value in graph[key]:
        queue.append(value)

    # while the queue is not empty
    while queue:
        # pop element from queue and store in popped
        popped:str|int = queue.popleft()
        # if popped is key, return True, there's a cycle from key to itself through at least 1 node
        if popped == key:
            return True
        # else, append all of popped's neighbors to the queue if not in hash_set already
        else:
            for value in graph[popped]:
                if value not in hash_set:
                    queue.append(value)
                    hash_set.add(value)

    # return False
    return False

    

# Part 4: ISCONNECTED
def isConnected(graph:dict[str|int, list[str|int]]) -> bool:
    # iterate through graph keys
    for key in graph:
        # iterate through graph keys
        for sec_key in graph:
            # avoid checking path between a node and itself
            if key == sec_key:
                continue
            # if no path exists between two keys, return False
            else:
                if findPathHelper(graph, key, sec_key) is False:
                    return False
    return True

def findPathHelper(graph:dict[str|int, list[str|int]], node1:str|int, node2:str|int) -> bool:
    # initialize a queue
    path_queue:deque[str|int] = deque()
    hash_set:set[int|str] = set()

    # push node1 to the queue
    path_queue.append(node1)
    hash_set.add(node1)
    # set a while loop that runs while the queue is not empty
    while len(path_queue) != 0:
        # pop element from queue
        popped:str|int = path_queue.popleft()
        # check if it's equal to node2, if yes, return True
        if popped == node2:
            return True
        # else, push the popped's neighbors
        for value in graph[popped]:
            if value not in hash_set:
                path_queue.append(value)
                hash_set.add(value)

    return False

# Part 5: TOPOSORT
"""def topoSort(graph:dict) -> list:
    return None
"""