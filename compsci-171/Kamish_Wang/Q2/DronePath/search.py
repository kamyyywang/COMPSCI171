import heapq
from collections import deque

def bfs_search(grid):
    start, goal = grid.start, grid.goal
    frontier = deque([start])
    came_from = {start: None}
    nodes_expanded = 0

    while frontier:
        current = frontier.popleft()
        nodes_expanded += 1

        if current == goal:
            break

        for neighbor in grid.neighbors(current):
            if neighbor not in came_from:
                frontier.append(neighbor)
                came_from[neighbor] = current

    # Reconstruct path
    if goal not in came_from:
        return [], float('inf'), nodes_expanded

    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = came_from[cur]
    path.reverse()

    cost = sum(grid.cost(p) for p in path)
    return path, cost, nodes_expanded



search_algorithm = bfs_search