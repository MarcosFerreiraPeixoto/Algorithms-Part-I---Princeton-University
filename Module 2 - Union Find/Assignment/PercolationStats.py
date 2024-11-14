import random
import math
import argparse
from Assignment.Percolation import Percolation

class PercolationStats():
    def __init__(self, n: int, trials: int):
        if n <= 0 or trials <=0:
            raise ValueError("The Grid size and the number of Trials must be above 0!")
        
        self.n = n
        self.trials_percolation_threshold = []
        trial_count = 0

        while trial_count < trials:
            p = self._run_trial()
            self.trials_percolation_threshold.append(p.number_of_open_sites()/self.n**2)

            trial_count += 1

    def _run_trial(self):
        p = Percolation(self.n)

        while not p.percolates():
            row = random.randint(1, self.n)
            col = random.randint(1, self.n)

            p.open(col, row)

        return p
    
    def mean(self):
        return sum(self.trials_percolation_threshold)/len(self.trials_percolation_threshold)
    
    def stddev(self):
        mean = self.mean()
        return math.sqrt(sum([(x - mean)**2 for x in self.trials_percolation_threshold])/(len(self.trials_percolation_threshold) - 1))
    
    def confidence_lo(self):
        return self.mean() - (self.stddev()/len(self.trials_percolation_threshold))

    def confidence_hi(self):
        return self.mean() + (self.stddev()/len(self.trials_percolation_threshold))


def main():
    parser = argparse.ArgumentParser(description="Estimate percolation threshold via Monte Carlo simulation.")
    parser.add_argument("grid_size", type=int, help="The size of the grid (n)")
    parser.add_argument("trials", type=int, help="The number of trials to run (T)")

    args = parser.parse_args()

    # Create a PercolationStats object and calculate results
    stats = PercolationStats(args.grid_size, args.trials)
    mean = stats.mean()
    stddev = stats.stddev()
    conf_lo = stats.confidence_lo()
    conf_hi = stats.confidence_hi()

    # Print the results
    print(f"mean                    = {mean}")
    print(f"stddev                  = {stddev}")
    print(f"95% confidence interval = [{conf_lo}, {conf_hi}]")

if __name__ == "__main__":
    main()