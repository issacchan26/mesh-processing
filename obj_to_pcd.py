import open3d as o3d
from os import listdir
from os.path import isfile, isdir, join
import numpy as np

input_path = "./input_obj"
output_path = "./output_pcd"
files = listdir(input_path)

for f in sorted(files):
  fullpath = join(input_path, f)
  if isfile(fullpath) and f.endswith(".obj"):
      mesh = o3d.io.read_triangle_mesh(fullpath)
      mesh.remove_duplicated_vertices()
      mesh.remove_duplicated_triangles()

      filename = f.split(".")[0]

      pcd = o3d.geometry.PointCloud()
      pcd.points = mesh.vertices
      pcd.colors = mesh.vertex_colors
      pcd.normals = mesh.vertex_normals

      # R = pcd.get_rotation_matrix_from_xyz((0, np.pi / 2, 0))
      # pcd.rotate(R, center=(0, 0, 0))

      pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])  # flip upside down along y axis

      o3d.io.write_point_cloud(output_path + "/" + filename + ".pcd", pcd, write_ascii=True)
