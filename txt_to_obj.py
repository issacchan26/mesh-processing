import os
from os import listdir
from os.path import isfile, isdir, join

mypath = "./vert_txt"
save_path = "./vert_xyz"
files = listdir(mypath)

for f in sorted(files):
    fullpath = join(mypath, f)
    if isfile(fullpath) and f.endswith(".txt"):
        input = open(fullpath)
        fout = open(save_path + "/" + f.split(".")[0] + ".xyz", "wt")
        for line in input:
            fout.write("%.6f %.6f %.6f\n" % (float(line.split(" ")[0]), float(line.split(" ")[1]), float(line.split(" ")[2])))
        input.close()
        fout.close()

import xyz_to_obj