import sys
import pymeshlab as ml
import os
from os import listdir
from os.path import isfile, isdir, join

mypath = "./mesh_data"
save_path = "./output_mesh"
files = listdir(mypath)

for f in sorted(files):
  fullpath = join(mypath, f)
  if isfile(fullpath) and f.endswith(".obj"):
    print("file：", f)
    head, filename = os.path.split(f)

    target_name = os.path.join(mypath, filename)

    ms = ml.MeshSet()
    ms.load_new_mesh(target_name)
    m = ms.current_mesh()
    print('input mesh has', m.vertex_number(), 'vertex and', m.face_number(), 'faces')

    # Target number of vertex
    TARGET = 10000

    # Estimate number of faces to have 100+10000 vertex using Euler
    numFaces = 100 + 2 * TARGET

    # Simplify the mesh. Only first simplification will be agressive
    while (ms.current_mesh().vertex_number() > TARGET):
        ms.apply_filter('simplification_quadric_edge_collapse_decimation', targetfacenum=numFaces, preservenormal=True)
        print("Decimated to", numFaces, "faces mesh has", ms.current_mesh().vertex_number(), "vertex")
        # Refine our estimation to slowly converge to TARGET vertex number
        numFaces = numFaces - (ms.current_mesh().vertex_number() - TARGET)

    m = ms.current_mesh()
    print('output mesh has', m.vertex_number(), 'vertex and', m.face_number(), 'faces')
    final_name = os.path.join(save_path, filename)
    ms.save_current_mesh(final_name)

