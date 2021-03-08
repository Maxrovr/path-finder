from collections import deque

class Node:
    def __init__(self, point, dist, parent = None):
        self.point  = point
        self.dist = dist
        self.parent = parent

class PathFinder:
    def find_path(self, source, destination, maze):
        sx, sy = source
        dx, dy = destination

        def is_inbounds(r, c):
            if r < 0 or c < 0 or r >= len(maze) or c >= len(maze[0]):
                return False
            return True

        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        bfs_queue = deque()
        visited = set()
        
        root = Node((sx, sy), 0)
        bfs_queue.append(root)

        while bfs_queue:
            curr = bfs_queue.popleft()

            if curr.point[0] == dx and curr.point[1] == dy:
                print(curr.dist)
                return curr
            
            for d in dirs:
                r = curr.point[0] + d[0]
                c = curr.point[1] + d[1]
                
                if is_inbounds(r, c) and (r,c) not in visited and maze[r][c] == 1:
                    visited.add((r,c))
                    bfs_queue.append(Node((r,c), curr.dist + 1, curr))
        return None

    def get_path(self, source, destination, maze):
        curr = self.find_path(source, destination, maze)
        path = set()
        while curr:
            path.add(curr.point)
            curr = curr.parent
        return path    

def display_path(path):
    if not path:
        print("No path found!")
        
    tile = "🟥"
    path_tile = "🔲"
    end_tile = "🟨"
    wall_tile = "⬛"
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) == source or (i, j) == destination:
                print(end_tile, end="")
            elif (i, j) in path:
                print(path_tile, end="")
            else:
                if maze[i][j] == 0:
                    print(wall_tile, end="")
                else:
                    print(tile, end="")
        print()

source = (0,0)
destination = (5,4)
mazes = [
    [[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
    [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ], 
    [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ], 
    [ 1, 0, 0, 0, 1, 0, 0, 0, 0, 1 ], 
    [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ], 
    [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 0 ], 
    [ 1, 0, 0, 0, 0, 0, 1, 1, 1, 1 ], 
    [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ], 
    [ 1, 0, 0, 0, 0, 0, 1, 0, 0, 1 ]],
    [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1 ],
    [ 0, 1, 1, 1, 1, 1, 0, 1, 0, 1 ],
    [ 0, 0, 1, 0, 1, 1, 1, 0, 0, 1 ],
    [ 1, 0, 1, 1, 1, 0, 1, 1, 0, 1 ],
    [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 1 ],
    [ 1, 0, 1, 1, 1, 0, 0, 1, 1, 0 ],
    [ 0, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 0, 0 ],
    [ 1, 1, 1, 1, 1, 0, 0, 1, 1, 1 ],
    [ 0, 0, 1, 0, 0, 1, 1, 0, 0, 1 ]]
    ]

pf = PathFinder()
for source, destination in [[(0,0),(5,4)],[(1,4),(8,8)]]:
    for maze in mazes:
        display_path(pf.get_path(source, destination, maze))
