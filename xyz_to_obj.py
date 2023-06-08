import pymeshlab as ml
import os
from os import listdir
from os.path import isfile, isdir, join

mypath = "./vert_xyz"
save_path = "./output_mesh"
files = listdir(mypath)

for f in sorted(files):
  fullpath = join(mypath, f)
  if isfile(fullpath) and f.endswith(".xyz"):

    head, name = os.path.split(f)

    target_name = os.path.join(mypath, name)

    ms = ml.MeshSet()
    ms.load_new_mesh(target_name)

    m = ms.current_mesh()

    filename = name.split(".")[0]
    filename = filename+'.obj'

    final_name = os.path.join(save_path, filename)
    ms.save_current_mesh(final_name)

