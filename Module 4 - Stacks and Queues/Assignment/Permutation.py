import sys
from Assignment.RandomizedQueue import RandomizedQueue

class Permutation:
    def __init__(self, n, file_name):
        self.randomized_queue = RandomizedQueue()
        self.n = n
        self.file_name = file_name
    
    def enqueue_from_file(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    for word in line.split(' '):
                        self.randomized_queue.enqueue(word)
        except FileNotFoundError:
            print(f"Error: The file {self.file_name} was not found.")
            sys.exit(1)

    def dequeue_and_print(self):
        for _ in range(self.n):
            if not self.randomized_queue.is_empty():
                print(self.randomized_queue.dequeue())
            else:
                break

def main():
    if len(sys.argv) != 3:
        print("Usage: python Permutation.py <n> <file_name>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])

        if n < 0:
            raise ValueError("Error: n must be a positive integer.")
    except ValueError:
        raise ValueError("Error: n must be an integer.")

    file_name = sys.argv[2]
    
    p = Permutation(n, file_name)
    p.enqueue_from_file()
    p.dequeue_and_print()

if __name__ == "__main__":
    main()
