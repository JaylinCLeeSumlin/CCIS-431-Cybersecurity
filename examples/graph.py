from collections import deque
import heapq

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
    
    def UCS(self, start_node, goal_node):
        priority_queue = []
        heapq.heappush(priority_queue , (0 , start_node))
        visited_node = set()

        # Maintian global cost
        gloabal_cost = {start_node: 0}

        while priority_queue:
            current_cost , current_node = heapq.heappop(priority_queue)

            if current_node == goal_node:
                return current_cost
            
            visited_node.add(current_node)

            for neighbor, cost in self.get(current_node):
                if neighbor not in visited_node:
                    new_cost = current_cost + cost
                    if neighbor not in gloabal_cost or new_cost < gloabal_cost[neighbor]:
                        gloabal_cost[neighbor] = new_cost
                        heapq.heappush(priority_queue)
        return None
    
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