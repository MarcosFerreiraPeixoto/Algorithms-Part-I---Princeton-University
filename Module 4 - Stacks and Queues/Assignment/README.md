# Programming Assignment 2: Queues

This assignment involves creating generic data types for a **Deque** and a **RandomizedQueue**.

### Deque
A double-ended queue supporting operations to add and remove items from both ends. Implement the following API:
- `public class Deque<Item> implements Iterable<Item>`
- Core methods: `addFirst`, `addLast`, `removeFirst`, `removeLast`
- Includes iterator and unit testing methods.

### RandomizedQueue
A queue allowing random item removal. Implement the following API:
- `public class RandomizedQueue<Item> implements Iterable<Item>`
- Core methods: `enqueue`, `dequeue`, `sample`
- Supports independent iterators in random order.

### Client Program - Permutation
Write `Permutation.java` that randomly selects and prints `k` items from input using either Deque or RandomizedQueue.

Refer to the full specification [here](https://coursera.cs.princeton.edu/algs4/assignments/queues/specification.php).
