import heapq
from heuristics import heuristic

def search_algorithm(grid):
    start =  grid.start
    goal = grid.goal
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), start))
    came_from = {start: None}
    g_score = {start: 0}
    nodes_expanded = 0
    while open_set:
        current_priority, current = heapq.heappop(open_set)

        if current == goal:
            break
        nodes_expanded += 1
        
        for neighbor in grid.neighbors(current):
            tentative_g_score = g_score[current] + grid.cost(neighbor)

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
                
    path = []
    current = goal
    if current not in came_from:
        return [], float('inf'), nodes_expanded
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path, g_score[goal], nodes_expanded
