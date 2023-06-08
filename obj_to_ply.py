import sys
import pymeshlab as ml
import os
from os import listdir
from os.path import isfile, isdir, join

mypath = "./input_obj"
save_path = "./output_ply"
files = listdir(mypath)

for f in sorted(files):
  fullpath = join(mypath, f)
  if isfile(fullpath) and f.endswith(".obj"):

    head, filename = os.path.split(f)

    target_name = os.path.join(mypath, filename)

    ms = ml.MeshSet()
    ms.load_new_mesh(target_name)
    m = ms.current_mesh()

    filename = filename.split('.')[0] + '.ply'

    final_name = os.path.join(save_path, filename)
    ms.save_current_mesh(final_name, binary=False, save_wedge_texcoord=False, save_vertex_color=True, save_face_color=False)

