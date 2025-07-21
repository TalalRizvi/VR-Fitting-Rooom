import numpy as np
import sys
import os

# Add the mesh directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mesh.mesh.mesh import Mesh

# Create a simple cube mesh
vertices = np.array([
    [0.5, -0.5, 0.5], [-0.5, -0.5, 0.5], [-0.5, 0.5, 0.5], [0.5, 0.5, 0.5],  # top face
    [0.5, -0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, 0.5, -0.5], [0.5, 0.5, -0.5]  # bottom face
])

faces = np.array([
    [0, 1, 2], [0, 2, 3],  # top face
    [4, 5, 6], [4, 6, 7],  # bottom face
    [0, 1, 5], [0, 5, 4],  # front face
    [2, 3, 7], [2, 7, 6],  # back face
    [0, 3, 7], [0, 7, 4],  # right face
    [1, 2, 6], [1, 6, 5]   # left face
])

# Create mesh object
cube_mesh = Mesh(v=vertices, f=faces)

# Try to display the mesh
try:
    cube_mesh.show()
    print("Mesh library is working correctly!")
except Exception as e:
    print(f"Error displaying mesh: {e}") 