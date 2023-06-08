from pytorch3d.io import load_obj, load_objs_as_meshes, save_obj


def clone_of_blender_shrink_fatten(target_mesh_path_='mesh_data_folder/1/1_140.obj', scale_factor_=0.01, out_name_='temp.obj'):
    chosen_meshs = load_objs_as_meshes(files=[target_mesh_path_], load_textures=False)
    # print(chosen_meshs[0].verts_normals_list()[0].size())
    # print(chosen_meshs[0].verts_list()[0].size())
    test_subject = chosen_meshs[0].verts_normals_list()[0]*scale_factor_
    # print(torch.sum(test_subject*test_subject, 1))
    # print(test_subject.size())
    new_mesh = chosen_meshs[0].clone()
    # print(new_mesh.verts_list()[0].size())
    new_mesh.verts_list()[0] = new_mesh.verts_list()[0] - test_subject
    save_obj(out_name_, new_mesh.verts_list()[0], new_mesh.faces_list()[0])
    return 0


if __name__ == '__main__':
    clone_of_blender_shrink_fatten()
