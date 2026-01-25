import os
import shutil
from copy_static import copy_files_recursive
from gen_content import generate_pages_recursive
import sys

def main():
    src = "./static"
    dst = "./docs"

    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    copy_files_recursive(src, dst)


    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"


    generate_pages_recursive(
        "content",
        "template.html",
        dst,
        basepath,
    )

    
if __name__ == "__main__":
    main()
