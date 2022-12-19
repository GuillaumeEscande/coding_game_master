from datetime import datetime
from cglogger import CGLogger

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent_node=None, case=None, distance=0):
        self.parent_node = parent_node
        self.case = case
        self.distance = distance

    def __eq__(self, other):
        return self.case.id == other.case.id

def astar(board, case_start, case_end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, case_start)
    end_node = Node(None, case_end)

    max_distance_search = board.get_fly_distance(case_start, case_end)

    # Initialize both open and closed list
    open_list = []
    closed_list_id = []

    # Add the start node
    open_list.append(start_node)

    cpt = 0

    # Loop until you find the end
    while len(open_list) > 0:
        cpt += 1

        open_list.sort(key=lambda x: x.distance)
        
        # Get the current node
        current_node = open_list.pop(0)
        closed_list_id.append(current_node.case.id)

        # Found the goal
        if current_node.case.id == end_node.case.id:
            path = []
            current = current_node
            while current is not None:
                path.append(current.case)
                current = current.parent_node
            return path[::-1] # Return reversed path
        
        for neighbor in board.get_neighbors(current_node.case): # Adjacent squares
            
            if neighbor.id not in closed_list_id:
                # Create new node
                distance = ((neighbor.x - end_node.case.x) ** 2) + ((neighbor.y - end_node.case.y) ** 2)
                if distance < max_distance_search +5:
                    neighbor_node = Node(current_node, neighbor, ((neighbor.x - end_node.case.x) ** 2) + ((neighbor.y - end_node.case.y) ** 2))

                    # Child is already in the open list
                    founded = False
                    for open_node in open_list:
                        if open_node.case.id == neighbor.id:
                            founded = True
                            if neighbor_node.distance < open_node.distance:
                                open_node.distance = neighbor_node.distance
                            break

                    if not founded:
                        # Add the child to the open list
                        open_list.append(neighbor_node)
        
    #CGLogger.debug("cpt ", case_start.x, ",", case_start.y, " ", case_end.x, ",", case_end.y, " ", current_node.case.x, ",", current_node.case.y, str(cpt))