# Shortest path in a maze – Lee Algorithm

Run using `python3 pathfinder.py`

### Problem
Given a 2-d maze in the form of the binary rectangular matrix, find the shortest path’s length in a maze from a given source to a given destination. Blocked nodes (Walls) are represented by a 0 and usable nodes(paths) by a 1

Lee's algorithm is optimal for maze routing problems where nodes are connected bu edges of equal weight. This algorithm is based on the Breadth–first search. It always gives an optimal solution, if one exists, but is slow and requires considerable memory.