import time
import random
import math
from puzzle import Puzzle

class PuzzleGenerator:
    def __init__(self, n_rows, n_columns, min_val, max_val):
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.min_val = min_val
        self.max_val = max_val
        self.max_time = 59.9

    def selective_successor(self, puzzle, samples=20):
        best_successor = None
        best_val = float('-inf')
        for _ in range(samples):
            successor = puzzle.get_random_successor()
            val = successor.get_value()
            if val > best_val:
                best_val = val
                best_successor = successor
        return best_successor, best_val

    def generate_puzzle(self) -> Puzzle:
        start_time = time.time()

        best_puzzle = Puzzle(self.n_rows, self.n_columns, self.min_val, self.max_val)
        best_puzzle.randomize()
        best_value = best_puzzle.get_value()

        temperature = 1000.0
        cooling_rate = 0.997

        current_puzzle = Puzzle(self.n_rows, self.n_columns, self.min_val, self.max_val)
        current_puzzle.randomize()
        current_value = current_puzzle.get_value()

        while time.time() - start_time < self.max_time:
            successor, successor_value = self.selective_successor(current_puzzle, samples=30)
            delta = successor_value - current_value

            if delta > 0 or random.random() < math.exp(delta / temperature):
                current_puzzle = successor
                current_value = successor_value

                if current_value > best_value:
                    best_puzzle = current_puzzle
                    best_value = current_value

            temperature *= cooling_rate

            if temperature < 1.0:
                for _ in range(2000):
                    successor, successor_value = self.selective_successor(current_puzzle, samples=30)
                    if successor_value > current_value:
                        current_puzzle = successor
                        current_value = successor_value
                        if current_value > best_value:
                            best_puzzle = current_puzzle
                            best_value = current_value

                temperature = 1000.0
                current_puzzle = Puzzle(self.n_rows, self.n_columns, self.min_val, self.max_val)
                current_puzzle.randomize()
                current_value = current_puzzle.get_value()

        return best_puzzle
        