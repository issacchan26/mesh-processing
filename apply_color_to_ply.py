import sys
import pymeshlab as ml
import os
from os import listdir
from os.path import isfile, isdir, join
import pandas as pd
import numpy as np

#  run "sed -i 's/[ \t]*$//' *.ply" inside folder

mypath = "./input_obj"
input_txt = './output_txt'
ply_without_color_path = "./ply_without_color"
ply_with_color_path = "./ply_with_color"
files = listdir(mypath)

color_array = [
[0, 0, 0],        # rest of body
[255, 255, 51],   # head
[102, 102, 0],    # neck
[255, 0, 0],      # right_shoulder
[255, 153, 153],  # left_shoulder
[255, 128, 0],    # right_upper_arm
[255, 204, 153],  # left_upper_arm
[204, 0, 102],    # right_elbow
[255, 102, 178],  # left_elbow
[128, 255, 0],    # right_fore_arm
[178, 255, 102],  # left_fore_arm
[204, 0, 204],    # right_wrist
[255, 102, 255],  # left_wrist
[0, 204, 0],      # right_hand
[102, 255, 102],  # left_hand
[255, 255, 255],  # main_body
[102, 0, 204],    # right_hip
[204, 153, 255],  # left_hip
[0, 204, 102],    # right_thigh
[102, 255, 178],  # left_thigh
[0, 0, 204],      # right_knee
[102, 102, 255],  # left_knee
[0, 204, 204],    # right_leg
[153, 255, 255],  # left_leg
[0, 102, 204],    # right_ankle
[153, 204, 255],  # left_ankle
[244, 244, 244],  # right_foot
[128, 128, 128]   # left_foot
]

for f in sorted(files):
  fullpath = join(mypath, f)
  if isfile(fullpath) and f.endswith(".obj"):

    head, filename = os.path.split(f)

    target_name = os.path.join(mypath, filename)

    ms = ml.MeshSet()
    ms.load_new_mesh(target_name)

    filename = filename.split('.')[0] + '.ply'

    final_name = os.path.join(ply_without_color_path, filename)
    ms.save_current_mesh(final_name, binary=False, save_wedge_texcoord=False, save_vertex_color=True, save_face_color=False)

files = listdir(input_txt)

for f in sorted(files):
  full_input_txt_path = join(input_txt, f)
  fname = f.split('.')[0]
  full_ply_without_color_path = ply_without_color_path + '/' + fname + '.ply'
  output_ply_with_color_path = ply_with_color_path + '/' + fname + '.ply'

  if isfile(full_input_txt_path) and f.endswith(".txt"):

    df1 = pd.read_csv(full_ply_without_color_path, sep=' ', names=['x', 'y', 'z', 'r', 'g', 'b'])

    df2 = pd.read_csv(full_input_txt_path, sep=' ', names=['x', 'y', 'z', 'label', 'r', 'g', 'b'])
    df2 = df2.iloc[:, 3:]

    for i in range(0, len(color_array)):
      df2.loc[df2['label'] == i, ['r', 'g', 'b']] = color_array[i]

    df2[['r', 'g', 'b']] = df2[['r', 'g', 'b']].astype('Int64')
    df2.index += 10
    df2 = df2.iloc[:, 1:]
    df1.update(df2)
    df1.loc[6.5] = ['property', 'uchar', 'red', np.nan, np.nan, np.nan]
    df1.loc[6.6] = ['property', 'uchar', 'green', np.nan, np.nan, np.nan]
    df1.loc[6.7] = ['property', 'uchar', 'blue', np.nan, np.nan, np.nan]
    df1 = df1.sort_index().reset_index(drop=True)
    df1.dropna()
    df1.to_csv(output_ply_with_color_path,  sep=' ', index=False, header=False, lineterminator='\n')
