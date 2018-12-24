# Vertices are a point in space
# There are 8 edges in a cube, so we first
# specify all 8 coordinates as vertices
DEFAULT_VERTICES = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# Edges are a line between 2 points/vertices.
# The number within the edge points to the index
# of the vertices
# E.G. (0,1) means its a line between vertex 0 and vertex 1
DEFAULT_EDGES = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)