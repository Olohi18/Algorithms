# Name:  - your name (and your partners name) <br>
# Peers:  - names of CSC252 students who you consulted or ``N/A'' <br>
# References:  - URL of resources used <br>
from hwk6 import *

def getSmallDirectedExample() -> dict[str|int, list[str|int]]:
    graph:dict[str|int, list[str|int]] = {}
    graph["you"] = ["alice", "bob"]
    graph["bob"] = ["peggy"]
    graph["alice"] = ["claire"]
    graph["claire"] = ["tom", "jonny"]
    graph["peggy"] = []
    graph["tom"] = []
    graph["jonny"] = []
    return graph


def main():
    POL_helper()    #Test is hwk6.py imported correctly.
    # Examples
    # Question: can a graph neither be undirected nor a DAG?
    dag_graph = getSmallDirectedExample()
    graph2:dict[str|int, list[str|int]] = {"a":["b", "c"], "b":["c"], "c":[]}
    graph3:dict[str|int, list[str|int]] = {"a":["b", "c"], "b":["c"], "c":["d"], "d":["a"]}
    graph4:dict[str|int, list[str|int]] = {"a":["b", "c"], "b":["c"], "c":["d"], "d":["a"], "e":["f", "g"], "f": ["g"], "g":["e", "f"]} # Disconnected and neither a DAG nor a bidirection
    graph5:dict[str|int, list[str|int]] = {"a":["b", "c"], "c":[], "d":[]} # Disconnected and DAG
    graph6:dict[str|int, list[str|int]] = {"a": ["b", "c"], "b": ["a", "c"], "c": ["a", "d"], "d": ["c"]}
    graph7:dict[str|int, list[str|int]] = {"a": ["b", "c"], "b": ["a", "c", "f"], "c": ["a", "b", "d", "f"], "d": ["c", "f"], "e": [], "f": ["c", "d", "e", "b"]}
    graph8:dict[str|int, list[str|int]] = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []} # multiple short paths (DAG form)
    graph9:dict[str|int, list[str|int]] = convertDAGToUG(graph8)
    graph10:dict[str|int, list[str|int]] = {"a": ["b", "c"], "b": ["d"], "c": ["d"]}
    graph11:dict[str|int, list[str|int]] = {"a": ["b", "g", "f"], "b": ["c"], "g":["c"], "c":["e"], "e":["f"]}
    print()
    print(f"-------- Convert DAG to Bidirected Graph ---------")
    print(f"DAG is {dag_graph}")
    print(f"Bidirected form is {convertDAGToUG(dag_graph)}")
    print(f"DAG is {graph2}")
    print(f"Bidirected form is {convertDAGToUG(graph2)}")
    print(f"DAG is {graph3}")
    print(f"Bidirected form is {convertDAGToUG(graph3)}")
    print(f"DAG is {graph5}")
    print(f"Bidirected form is {convertDAGToUG(graph5)}")
    print()

    print(f"-------- findBFSPath Test ----------")
    print(f"Path is {findBFSPath(dag_graph, "alice", "jonny")}")
    print(f"Path is {findBFSPath(convertDAGToUG(dag_graph), "alice", "jonny")}") # UG equivalent of dag_graph
    print(f"Path is {findBFSPath(graph2, "a", "c")}") # Path fron node to direct neighbor
    print(f"Path is {findBFSPath(dag_graph, "alice", "alice")}") # Path from node to itself
    print(f"Path is {findBFSPath(graph6, "a", "d")}") #
    print(f"Path is {findBFSPath(graph7, "a", "e")}")
    print(f"Path is {findBFSPath(graph8, "a", "d")}") # multiple shortest paths (DAG form)
    print(f"Path is {findBFSPath(graph9, "a", "d")}") # multiple shortest paths (UG form)
    print()

    print(f"-------- IsCyclic Test --------")
    print(f"Graph is cyclic: {isCyclic(dag_graph)}") # False
    print(f"Graph is cyclic: {isCyclic(convertDAGToUG(dag_graph))}") # True
    print(f"Graph is cyclic: {isCyclic(graph2)}") # False  
    print(f"Graph is cyclic: {isCyclic(graph3)}") # True
    print()

    print(f"------- isConnected Test -------")
    print(f"Graph2 is {graph2}")
    print(f"Graph2 is connected: {isConnected(convertDAGToUG(graph2))}") # True
    print(f"Graph3 is connected: {isConnected(convertDAGToUG(graph3))}") # True
    print(f"Dag Graph is connected: {isConnected(convertDAGToUG(dag_graph))}") # True
    print(f"Graph5 is connected: {isConnected(convertDAGToUG(graph5))}") # False
    print(f"Graph3 is connected: {isConnected(convertDAGToUG(graph4))}") # False
    print()

    print(f"------- Topological Sort --------")
    print(f"Topological Sorted is {topoSort(graph10)}")
    print(f"Topological Sorted is {topoSort(graph11)}")
    


if __name__ == "__main__":
    main()