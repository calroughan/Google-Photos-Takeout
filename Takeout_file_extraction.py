import os
import shutil

# Steps for next time
# Run File_Types.py to figure out which file types exist in the directory first,
# Some code to loop over all dir types would be very useful

# Also, instead of appending to a duplicates tab, just add a suffix of "(dup)" to the file name
# to avoid having to manually do it

src_dir = "D:\\Photos\\Google_Photos_13_7_2020"
dest_dir = "D:\\Photos\\13_7_2020"

duplicates = []

# Get the subdirectories
subdirs = [x[0] for x in os.walk(src_dir)]

for currdir in subdirs[1:]:
    allfiles = os.listdir(currdir)
    for pics in allfiles:
        if pics[-4:] == ".PNG":
            print(currdir + os.sep + pics)

            # Check that there is not already a file with that name in the dest_dir
            if not os.path.isfile(dest_dir + os.sep + pics):
                shutil.copy(currdir + os.sep + pics, dest_dir + os.sep + pics)

            # Else append filename to a list
            else:
                duplicates.append(currdir + os.sep + pics)
