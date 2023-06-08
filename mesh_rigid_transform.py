import pymeshlab as ml
import random
import os
from os import listdir
from os.path import isfile, isdir, join

input_path = "./mesh_data"
output_path = "./output_mesh"
files = listdir(input_path)

def rotate_mesh(input_mesh, filename):

    rotate_axis = 1                                                               # x = 0, y = 1, z = 2
    rotate_angle = random.randint(-45, 45)                                        # from 45 to -45

    filename = filename.split(".")[0] + "_r_" + str(rotate_angle) + ".obj"
    output_mesh = os.path.join(output_path, filename)
    ms.load_new_mesh(input_mesh)
    ms.apply_filter('compute_matrix_from_rotation', rotaxis=rotate_axis, rotcenter=0, angle=rotate_angle)
    ms.save_current_mesh(output_mesh)
    return

def translate_mesh(input_mesh, filename):

    translate_distance_x = round(random.uniform(-0.50, 0.50), 2)                  # shift x distance from -0.50 to 0.50
    translate_distance_z = round(random.uniform(-0.50, 0.50), 2)                  # shift z distance from -0.50 to 0.50

    filename = filename.split(".")[0] + "_t_x_" + str(translate_distance_x) + "_z_" + str(translate_distance_z) + ".obj"
    output_mesh = os.path.join(output_path, filename)
    ms.load_new_mesh(input_mesh)
    ms.apply_filter('compute_matrix_from_translation', axisx=translate_distance_x, axisz=translate_distance_z)
    ms.save_current_mesh(output_mesh)
    return

def scale_mesh(input_mesh, filename):

    scale_parameter = round(random.uniform(0.60, 0.90), 2)                        # scale from 0.60 to 0.90

    filename = filename.split(".")[0] + "_s_" + str(scale_parameter) + ".obj"
    output_mesh = os.path.join(output_path, filename)
    ms.load_new_mesh(input_mesh)
    ms.apply_filter('compute_matrix_from_scaling_or_normalization', axisx=scale_parameter, uniformflag=1)
    ms.save_current_mesh(output_mesh)
    return

for f in sorted(files):
  fullpath = join(input_path, f)
  if isfile(fullpath) and f.endswith(".obj"):
      head, filename = os.path.split(f)
      input_mesh = os.path.join(input_path, filename)
      ms = ml.MeshSet()
      # rotate_mesh(input_mesh, filename)
      # translate_mesh(input_mesh, filename)
      scale_mesh(input_mesh, filename)





