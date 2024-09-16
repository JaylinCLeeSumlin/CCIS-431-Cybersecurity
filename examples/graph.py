class Graph:
    def __init__(self) -> None:
        self.edges = {}

    def add_edges(self, from_node, to_node, weight):
        
        # if the from node is not in the graph, add it with no following node connected
        if from_node not in self.edges:
            self.edges[from_node] = []
        
        # add a node to an existing node
        self.edges[from_node].append((to_node, weight))