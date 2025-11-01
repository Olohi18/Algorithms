# Name:  Olohi John
# Peers: Catherine Weeks
# References:  
from collections import deque
# Assumption: Keys, which are leaf nodes in the graph, are simply included as a key in the adjacency list with a value of '[]', an empty list
# Assumption: nodes passed as parameters into the functions are guaranteed to be keys in the graph, ie no need to check the edge 
# case of whether a parameter node is in the graph

#### DO NOT EDIT - START ####
def POL_helper():
    print("File Imported")
#### DO NOT EDIT - END ####

# Part 1: DAG2UG
def convertDAGToUG(dag_graph:dict[str|int, list[str|int]]) -> dict[str|int, list[str|int]]: 
    """
    Converts a DAG to an undirected graph

    @param dag_graph: (dict) an adjacency list representation of a DAG
    @return ug: (dict) an adjacency list representation of the resulting undirected graph

    >>> convertDAGToUG({'a': ['b', 'c'], 'b': ['c'], 'c': []})
    {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['a', 'b']}
    """
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
    """
    Helper function that returns whether or not an element is in an array

    @param val: (str) the element whose containment in array is to be checked
    @param array: (list) the array to be searched

    >>> isIn(5, [2, 5, 7])
    False
    """
    for elem in array:
        if elem == val:
            return True

    return False



# Part 2: BFS            
def findBFSPath(graph:dict[str|int, list[str|int]], start_node:str, end_node:str) -> list[str|int] | None:
    """
    Returns the shortest path between two nodes in a graph

    @param graph: (dict) an adjacency list representation of the graph
    @param start_node, end_node: (str), (str) the nodes whose shortest path between is to be returned

    >>> findBFSPath(['alice', 'bob'], 'bob': ['peggy'], 'alice': ['claire'], 'claire': ['tom', 'jonny'], 'peggy': [], 'tom': [], 'jonny': []}, 'alice', 'jonny')
    ['alice', 'claire', 'jonny']
    """
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
    """
    Helper function that returns the path between two nodes, given their backtracking hashmap

    @param visited: (dict) a map of node, prev pairs
    @param popped: (str|int) the node to start backtracking from
    @param start: (str|int) the node to stop backtracking at

    >>> path({'b': 'a', 'c': 'a', 'a': 'b', 'd': 'b'}, d)
    ['a', 'b', 'd']
    """
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
    """
    Returns whether or not a graph contains a cycle

    @param graph: (dict) an adjacency list representation of the graph

    >>> isCyclic({"a":["b", "c"], "b":["c"], "c":["d"], "d":["a"]})
    True
    """
    # iterate through keys in the graph
    for key in graph:
        # if findPath(key, key) == True, return False
        if isCylicHelper(key, graph) == True:
            return True
    # return True
    return False

def isCylicHelper(key:str|int, graph:dict[str|int, list[str|int]]) ->bool:
    """
    Helper function that checks if you can traverse back to a key from itself

    @param key: (str|int) a key in the graph
    @param graph: (dict) an adjacency list represenation of the graph

    >>> ('a', {"a":["b", "c"], "b":["c"], "c":["d"], "d":["a"]})
    True
    """
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
    """
    Checks if a graph is connected

    @param graph: (dict) an adjacency list representation of the graph

    >>> isConnected({'a': ['b', 'c'], 'b': ['c'], 'c': []})
    True
    """
    start:str|int = list(graph)[0]
    queue:deque[str|int] = deque()
    set_store:set[str|int] = set()
    queue.append(start)
    set_store.add(start)

    while queue:
        popped:str|int = queue.popleft()
        for n in graph[popped]:
            if n not in set_store:
                queue.append(n)
                set_store.add(n)

    return len(set_store) == len(graph)

# Part 5: TOPOSORT
def topoSort(graph:dict[str|int, list[str|int]]) -> list[str|int]:
    """
    Returns the nodes in a graph in topological order

    @param graph: (dict) an adjacency list represenation of a graph
    @return sorted: (list) a list of the vertices in the input graph, sorted topologically

    >>> topoSort({"a": ["b", "c"], "b": ["d"], "c": ["d"]})
    [a, b, c, d]
    """
    sorted:list[str|int] = []
    visited:set[str|int] = set()
    for key in graph:
        if key not in visited:
            visited.add(key)
            helperTopo(graph, key, sorted, visited)
    return sorted

def helperTopo(graph:dict[str|int, list[str|int]], key:str|int, sorted:list[str|int], visited:set[str|int]) -> None:
    """
    Helper function that appends performs a DFS on the graph and appends its nodes to a list topologically

    @param graph: (dict) an adjacency list represenation of a graph

    >>> topoSort({"a": ["b", "c"], "b": ["d"], "c": ["d"]})
    """
    neighbors = graph[key] if key in graph else []
    for n in neighbors:
        if n not in visited:
            visited.add(n)
            helperTopo(graph, n, sorted, visited)
    sorted.insert(0, key)


"""def topoSort(graph:dict[str|int, list[str|int]]) -> list[str|int]:
    sorted:list[str|int] = []
    visited:set[str|int] = set()
    for key in graph:
        if key not in visited:
            visited.add(key)
            result:list[str|int] = helperTopo(graph, key, visited)
            print(f"result is {result}")
            sorted += [key] + result

    return sorted

def helperTopo(graph:dict[str|int, list[str|int]], key:str|int, visited:set[str|int]) -> list[str|int]:
    neighbors:list[str|int] = []
    if key not in graph:
        return []
    neighbors:list[str|int] = graph[key]
    print(f"neighbors are {neighbors}")
    visited.add(key)
    result:list[str|int] = []
    for n in neighbors:
        if n not in visited:
            result += [n]
    for n in neighbors:
        if n not in visited:
            visited.add(n)
            result += helperTopo(graph, n, visited)
    return result"""


