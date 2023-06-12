# CPII mesh processing
This repo is to provide a series of algorithm to process mesh and point cloud files. \
It provides format transfer, mesh simplification, mesh rigid transform and annotation transform 

## Installation

Use the pip to install dependencies, you may use conda instead \
For PyTorch3D, please follow this link to install: https://github.com/facebookresearch/pytorch3d/blob/main/INSTALL.md

```bash
pip install numpy
pip install pandas
pip install pymeshlab
pip install open3d
```

## mesh format convert
[obj to pcd format](./obj_to_pcd.py) \
[obj to ply format](./obj_to_ply.py)

## txt convert into obj mesh
[txt to obj format](./txt_to_obj.py) \
[xyz to obj format](./xyz_to_obj.py)

## mesh rigid transform
[mesh augmentation](./mesh_rigid_transform.py) \
[shrink and flatten function in Blender](./shrink_flatten.py)

## mesh annotation operation
[output the annotation to simplified txt](./annotation_output.py) \
[add rgb value into ply file](./apply_color_to_ply.py)
