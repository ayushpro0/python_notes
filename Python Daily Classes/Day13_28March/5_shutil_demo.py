import shutil
shutil.copy("output_file.txt", "target.txt")

"""
shutil.copy2(src, dst)
similar to shutil.copy(), but metadata is copied as well in fact, this is just shutil.copy() followed by copystat()
"""

#shutil.copytree('c:/Jan_IntPython', 'c:/Python_testing55')
"""
recursively copy an entire directory tree rooted at src.
The destination directory, named by dst, must not already exist; it will be created as well as missing parent directories.
Permissions and times of directories are copied with copystat(), individual files are copied using shutil.copy2()
"""

# shutil.rmtree("c:/Python_testing2")
"""
Delete an entire directory tree
"""