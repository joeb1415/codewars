"""
http://www.codewars.com/kata/escape-the-mines
"""

from collections import deque


left = 'left'
right = 'right'
up = 'up'
down = 'down'



def solve(map, miner, exit):
    start_square = Square(miner['x'], miner['y'], [], [])

    xy_visited = set()
    xy_visited.add((start_square.x, start_square.y))

    squares_to_visit = deque()
    squares_to_visit.append(start_square)

    while len(squares_to_visit) > 0:
        square = squares_to_visit.popleft()
        xy_visited.add((square.x, square.y))

        if square.x == exit['x'] and square.y == exit['y']:
            return square.path

        for neighbor in square.get_neighbors(map):
            if (neighbor.x, neighbor.y) not in xy_visited:
                squares_to_visit.append(neighbor)

    raise ValueError('No path found from miner to exit')


class Square:
    def __init__(self, x, y, history, path):
        self.x = x
        self.y = y
        self.history = history  # list of Squares visited, not including self
        self.path = path  # list of left, right, up, down moves

    def make_neighbor(self, direction):
        x = self.x
        y = self.y
        
        if direction == left: x = self.x - 1
        if direction == right: x = self.x + 1
        if direction == up: y = self.y - 1
        if direction == down: y = self.y + 1
        
        history = self.history + [self]
        path = self.path + [direction]
        
        neighbor = Square(x, y, history, path)
        
        return neighbor

    def get_neighbors(self, map):
        x = self.x
        y = self.y

        width = len(map)
        height = len(map[0])

        open_neighbors = []

        if x > 0 and map[x-1][y]:
            open_neighbors.append(self.make_neighbor(left))
        if x < width - 1 and map[x+1][y]:
            open_neighbors.append(self.make_neighbor(right))
        if y > 0 and map[x][y-1]:
            open_neighbors.append(self.make_neighbor(up))
        if y < height - 1 and map[x][y+1]:
            open_neighbors.append(self.make_neighbor(down))

        return open_neighbors
