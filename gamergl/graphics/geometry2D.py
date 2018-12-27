from OpenGL import GL


def get_perimeter_edges(vertices):
    return [(i, i+1) for i in range(len(vertices) - 1)]\
           + [(len(vertices) - 1, 0)]


def line_definition(edges, vertices):
    def definition(center, rotation, scale):
        new_vertices = [
            (vertex[0] * scale[0] + center[0],
            vertex[1] * scale[1] + center[1],
            0)
            for vertex in vertices
        ]

        GL.glBegin(GL.GL_LINES)
        for edge in edges:
            for v in edge:
                vertex = new_vertices[v]
                GL.glVertex3fv(vertex)
        GL.glEnd()
    
    # return the function
    return definition


square_vertices = (
    (1, 1),
    (-1, 1),
    (-1, -1),
    (1, -1)
)


square_edges = get_perimeter_edges(square_vertices)
square_definition = line_definition(square_edges, square_vertices)


triangle_vertices = (
    (0, 1),
    (-0.5, -0.5),
    (0.5, -0.5)
)


triangle_edges = get_perimeter_edges(triangle_vertices)
triangle_definition = line_definition(triangle_edges, triangle_vertices)