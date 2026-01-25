import os
import shutil
from copy_static import copy_files_recursive
from gen_content import generate_pages_recursive

def main():
    src = "./static"
    dst = "./public"

    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    copy_files_recursive(src, dst)


    generate_pages_recursive(
        "content",
        "template.html",
        "public"
    )

    
if __name__ == "__main__":
    main()
