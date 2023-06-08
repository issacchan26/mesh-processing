from os import listdir
from os.path import isfile, isdir, join
import pandas as pd
import numpy as np

"""
Convert the annotation txt file for pyg training, 
by combining the annotation txt from semantic segmentation editor and original obj file
the point order will follow the obj file
please remind that the script will not overwrite the existing file, 
please clean the folder before running the script

this script will call apply_color_to_ply.py at the end, no need to run the script separately
"""


input_txt = './input_annotated_txt'
input_obj = './input_obj'
output_txt = './output_txt'

files = listdir(input_txt)

for f in sorted(files):
  fullpath = join(input_txt, f)
  fname = f.split('.')[0]
  obj_path = input_obj + '/' + fname + '.obj'
  output_path = output_txt + '/' + fname + '.txt'
  if isfile(fullpath) and f.endswith('.txt'):

      df1 = pd.read_csv(obj_path, sep=' ', names=['type', 'x', 'y', 'z'], on_bad_lines='skip')
      df1 = df1.loc[df1['type'] == 'v']
      df1 = df1.reset_index(drop=True)
      df1['xyz'] = df1['x'].astype(str) + df1['y'].astype(str) + df1['z'].astype(str)
      df1.set_index('xyz', inplace=True)

      df2 = pd.read_csv(fullpath, sep=" ", skiprows=10, names=['x', 'y', 'z', 'label', 'object'])
      df2 = df2.drop_duplicates()
      df2 = df2.reset_index(drop=True)
      df2['y'] = df2['y'] * (-1)
      df2 = df2.round(6)
      df2['xyz'] = df2['x'].map('{:,.6f}'.format) + df2['y'].map('{:,.6f}'.format) + df2['z'].map('{:,.6f}'.format)
      df2.set_index('xyz', inplace=True)
      df2 = df2.drop_duplicates()
      df2 = df2.reindex(df1.index)
      df2 = df2.drop('object', axis=1)
      df2 = df2.reset_index()
      df2 = df2.drop('xyz', axis=1)
      df2.to_csv(output_path, header=None, index=None, sep=' ', mode='x')

import apply_color_to_ply



