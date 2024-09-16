from collections import deque

class Graph:
    def __init__(self) -> None:
        self.edges = {}

    def add_edges(self, from_node, to_node, weight):

        # if the from node is not in the graph, add it with no following node connected
        if from_node not in self.edges:
            self.edges[from_node] = []
        
        # add a node to an existing node
        self.edges[from_node].append((to_node, weight))

    def get(self, current_node):
        return self.edges[current_node]
    
    def BFS(self, start_node, goal_node):
        # Implement deque data structure for BFS
        queue = deque([start_node])

        # Keep track of visited nodes, use set to avoid duplicated visits
        visited_nodes = set()

        while queue:
            # Use popleft() to implement LILO
            current_node = queue.popleft()

            # Return current node if it is the goal node
            if current_node == goal_node:
                return current_node
            
            # If current node is not the goal, add it to the set of visited nodes
            visited_nodes.add(current_node)

            for neighbor, _ in self.get(current_node):
                # If neighboring nodes have not been visited, add to queue to be visited
                if neighbor not in visited_nodes:
                    queue.append(neighbor)
        
        # Return nothing if goal node is not present in graph
        return
    
if __name__ == "__main__":

    # Initilize graph
    graph = Graph()

    # Add nodes with format (from_node, to_node, weight)
    graph.add_edges("A","B", 1)
    graph.add_edges("A","C", 3)
    graph.add_edges("B","D", 1)
    graph.add_edges("C","D", 1)
    graph.add_edges("B","E", 1)
    graph.add_edges("D","E", 1)

    # Search graph for node E stating at node C
    if graph.BFS("C","E"):
        print("Found goal state: E")
    else:
        print("Goal state not found: E")