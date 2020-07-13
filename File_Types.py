import os
import shutil

src_dir = "D:\\Photos\\Google_Photos_13_7_2020"

file_types = []

# Get the subdirectories
subdirs = [x[0] for x in os.walk(src_dir)]

# Step over all subdirectories
for currdir in subdirs[1:]:
    allfiles = os.listdir(currdir)
    for currfile in allfiles:

        # Extract the extension
        filename, file_extension = os.path.splitext(currdir + os.sep + currfile)

        # Check that there is not already a file with that name in the dest_dir
        if file_extension not in file_types:
            file_types.append(file_extension)

print(file_types)
