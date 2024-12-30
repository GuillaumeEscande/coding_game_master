import numpy 



class Cell(object):
    index: int
    cell_type: int
    resources: int
    neighbors: list[int]
    my_ants: int
    opp_ants: int

    def __init__(self, index: int, cell_type: int, resources: int, neighbors: list[int], my_ants: int, opp_ants: int):
        self.index = index
        self.cell_type = cell_type
        self.resources = resources
        self.neighbors = neighbors
        self.my_ants = my_ants
        self.opp_ants = opp_ants



def floyd_marshall(graph: list[Cell]) -> list[list[int]]:
    n = len(graph)
    dist = numpy.full((n, n), INF)

    # Initialisation de la matrice de distance avec les poids des arêtes existantes
    for u in range(n):
        cell: Cell = graph[u]
        dist[u][u] = 0
        for v in cell.neighbors:
            if v >= 0 :
                dist[u][v] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])

    return dist



class Board(object):
    number_of_cells: int
    cells: list[Cell]
    distances: list[list[int]]
    total_cristal: int
    target_score: int

    def __init__(self):
        self.cells = []
        self.number_of_cells = int(input())
        total_cristal_ressources = 0
        for i in range(self.number_of_cells):
            inputs = [int(j) for j in input().split()]
            cell_type = inputs[0] # 0 for empty, 1 for eggs, 2 for crystal
            initial_resources = inputs[1] # the initial amount of eggs/crystals on this cell
            neigh_0 = inputs[2] # the index of the neighbouring cell for each direction
            neigh_1 = inputs[3]
            neigh_2 = inputs[4]
            neigh_3 = inputs[5]
            neigh_4 = inputs[6]
            neigh_5 = inputs[7]
            cell: Cell = Cell(
                index = i,
                cell_type = cell_type,
                resources = initial_resources,
                neighbors = [neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5],
                my_ants = 0,
                opp_ants = 0
            )
            self.cells.append(cell)
            if cell_type == 2 :
                total_cristal_ressources += initial_resources

        self.distances = floyd_marshall(self.cells)
        self.total_cristal = total_cristal_ressources
        self.target_score = (total_cristal_ressources / 2)+1

    def read_state(self):
        self.total_cristal = 0
        for i in range(self.number_of_cells):
            inputs = [int(j) for j in input().split()]
            resources = inputs[0] # the current amount of eggs/crystals on this cell
            my_ants = inputs[1] # the amount of your ants on this cell
            opp_ants = inputs[2] # the amount of opponent ants on this cell

            self.cells[i].resources = resources
            self.cells[i].my_ants = my_ants
            self.cells[i].opp_ants = opp_ants
            if self.cells[i].cell_type == 2 :
                self.total_cristal += resources
        
