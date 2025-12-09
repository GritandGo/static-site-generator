import os
import shutil


def copy_files_recursive(src, dst):
    """
    Recursively copies all files and subdirectories from a source 
    directory to a destination directory.

    If the destination directory (dst) does not exist, it will be 
    created. Note that this function requires deleting the existing 
    'public' directory first, which should be handled outside this call 
    in main().

    :param src: The path to the source directory (e.g., './static').
    :param dst: The path to the destination directory (e.g., './public').
    :raises FileNotFoundError: If the source directory does not exist.
    """

    if not os.path.exists(src):
        raise FileNotFoundError(f"Source directory does not exist: {src}")


    # if destination directory does not exist, creates directory
    if not os.path.exists(dst):
        os.mkdir(dst)

    # get item name
    for name in os.listdir(src):


        # build full path to item
        src_path = os.path.join(src, name)


        # ***check if full path is a file***
        if os.path.isfile(src_path): # returns True for files directly in src
            print(f"File found: {src_path}")

            # create destination path
            dst_path = os.path.join(dst, name)

            # copy file
            shutil.copy(src_path, dst_path)

        # ***check if full path is a directory***
        elif os.path.isdir(src_path):
            dst_subdir = os.path.join(dst, name)
            if not os.path.exists(dst_subdir):
                os.mkdir(dst_subdir)
            copy_files_recursive(src_path, dst_subdir)



