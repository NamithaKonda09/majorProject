import os
def read_dir():
    
    path = "datasets"
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        files.append(f)
    print(files)
read_dir()

