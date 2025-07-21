import numpy as np
import mesh
import os

def test_mesh_shape(file_path):
    print(f"\nTesting mesh from file: {file_path}")
    
    # Load the mesh
    m = mesh.Mesh(file_path)
    print(f"Mesh loaded successfully")
    
    # Test basic properties
    print(f"Number of vertices: {m.vertices.shape[0]}")
    print(f"Number of faces: {m.faces.shape[0]}")
    
    # Test vertex operations
    print("\nTesting vertex operations:")
    print(f"First vertex: {m.vertices[0]}")
    print(f"Last vertex: {m.vertices[-1]}")
    
    # Test face operations
    print("\nTesting face operations:")
    print(f"First face: {m.faces[0]}")
    print(f"Last face: {m.faces[-1]}")
    
    # Test bounding box
    bbox = m.bounding_box()
    print("\nBounding box:")
    print(f"Min: {bbox[0]}")
    print(f"Max: {bbox[1]}")
    
    # Test face normals
    print("\nTesting face normals:")
    print(f"First face normal: {m.face_normals[0]}")
    
    # Test vertex normals
    print("\nTesting vertex normals:")
    print(f"First vertex normal: {m.vertex_normals[0]}")
    
    return True

def main():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mesh_dir = os.path.join(current_dir, "mesh", "mesh")
    
    # List of mesh files to test
    mesh_files = [
        "cube.obj",
        "colored_cube.obj"
    ]
    
    print("Starting mesh shape tests...")
    
    for mesh_file in mesh_files:
        file_path = os.path.join(mesh_dir, mesh_file)
        if os.path.exists(file_path):
            try:
                success = test_mesh_shape(file_path)
                if success:
                    print(f"\n✅ Test passed for {mesh_file}")
                else:
                    print(f"\n❌ Test failed for {mesh_file}")
            except Exception as e:
                print(f"\n❌ Error testing {mesh_file}: {str(e)}")
        else:
            print(f"\n❌ Mesh file not found: {mesh_file}")
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    main() 