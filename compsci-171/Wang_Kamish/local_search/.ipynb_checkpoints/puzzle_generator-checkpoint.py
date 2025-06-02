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

        temperature = 1000.0  # High initial temperature
        cooling_rate = 0.997  # Balanced cooling rate

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

            # Aggressive hill-climbing every time temperature gets moderately low
            if temperature < 1.0:
                for _ in range(2000):  # Increased hill-climbing intensity
                    successor, successor_value = self.selective_successor(current_puzzle, samples=30)
                    if successor_value > current_value:
                        current_puzzle = successor
                        current_value = successor_value
                        if current_value > best_value:
                            best_puzzle = current_puzzle
                            best_value = current_value

                # After hill-climbing, restart with high temperature again
                temperature = 1000.0
                current_puzzle = Puzzle(self.n_rows, self.n_columns, self.min_val, self.max_val)
                current_puzzle.randomize()
                current_value = current_puzzle.get_value()

        return best_puzzle

    """
        return self.random_walk(random_walk_time)  # Do a random walk for some time and return the solution

    def random_walk(self, time_limit: float) -> Puzzle:
        # A very simple function that starts at a random configuration and keeps randomly modifying it
        # until it hits the time limit. Returns the best solution found so far.
        
        p = Puzzle(self.n_rows, self.n_columns, self.min_val, self.max_val)  # Generate a random puzzle
        
        # Keep track of the best puzzle found so far (and its value)
        best_puzzle = p
        best_value = p.get_value()
        
        # Keep track of the time so we don't exceed it
        start_time = time.time()
        
        # Loop until we hit the time limit
        while time.time() - start_time < time_limit - 0.1:  # To make sure we don't exceed the time limit
            # Generate a successor of p by randomly changing the value of a random cell
            # (since we are doing a random walk, we just replace p with its successor)
            p = p.get_random_successor()
            value = p.get_value() 
            
            # Update the current best solution
            if value > best_value:  
                best_value = value  
                best_puzzle = p
        
        return best_puzzle 
   """
