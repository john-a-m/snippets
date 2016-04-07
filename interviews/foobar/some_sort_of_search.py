import heapq

class Graph(object):

    def __init__(self, grid, x, y, steps_left):
        self.x = x
        self.y = y
        self.grid = grid
        self.cost = grid[y][x]
        self.steps_left = steps_left

    @property
    def children(self):
        children = []
        if self.x + 1 < len(self.grid):
            right = Graph(self.grid, self.x + 1, self.y, self.steps_left - 1)
            children.append(right)

        if self.y + 1 < len(self.grid):
            down = Graph(self.grid, self.x, self.y + 1, self.steps_left - 1)
            children.append(down)

        return children


def answer(food, grid):

    N = len(grid)
    root = Graph(grid, 0, 0, N)
    frontier = [(food, root)]

    while frontier:
        (current_food, node) = heapq.heappop(frontier)
        for child in node.children:
            food = current_food - child.cost
            if food < 0 or food - child.steps_left < 0:
               continue
            elif child.x == child.y == N - 1:
                return food
            else:
                heapq.heappush(frontier, (food, child))

    return -1

if __name__ == "__main__":
    
    print answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
    print answer(12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
    
