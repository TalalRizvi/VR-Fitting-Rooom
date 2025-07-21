import numpy as np
from psbody.mesh import Mesh, MeshViewers
import os
import threading
import time
import signal
import sys

def signal_handler(sig, frame):
    print('\nClosing viewer...')
    sys.exit(0)

def create_cube():
    vertices = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ])
    
    faces = np.array([
        [0, 1, 2],
        [0, 2, 3],
        [4, 5, 6],
        [4, 6, 7],
        [0, 1, 5],
        [0, 5, 4],
        [2, 3, 7],
        [2, 7, 6],
        [0, 3, 7],
        [0, 7, 4],
        [1, 2, 6],
        [1, 6, 5]
    ])
    
    return Mesh(v=vertices, f=faces)

def rotate_mesh(mesh, angle):
    """Rotate mesh around Y axis"""
    rotation_matrix = np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])
    new_vertices = np.dot(mesh.v, rotation_matrix.T)
    return Mesh(v=new_vertices, f=mesh.f)

def update_viewer(mvs, mesh):
    angle = 0
    try:
        while True:
            # Rotate mesh
            angle += 0.02
            rotated_mesh = rotate_mesh(mesh, angle)
            
            # Update viewer
            mvs[0][0].set_static_meshes([mesh])
            mvs[0][1].set_static_meshes([rotated_mesh])
            
            time.sleep(0.03)  # 30 FPS approximately
    except KeyboardInterrupt:
        print("\nAnimation stopped")

def main():
    # Set up signal handler for graceful exit
    signal.signal(signal.SIGINT, signal_handler)
    
    # Create mesh
    cube = create_cube()
    
    # Create viewer
    mvs = MeshViewers((1, 2))
    
    print("\nViewer controls:")
    print("- Left mouse button: Rotate")
    print("- Middle mouse button: Zoom")
    print("- Right mouse button: Pan")
    print("- Press Ctrl+C to exit")
    
    # Start animation in a separate thread
    animation_thread = threading.Thread(target=update_viewer, args=(mvs, cube))
    animation_thread.daemon = True
    animation_thread.start()
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main() 