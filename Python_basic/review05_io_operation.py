import os
import shutil

def copy_single_file(source_file, dest_file):
    with open(source_file, 'rb') as f1, open(dest_file, 'wb') as f2:
        while True:
            content = f1.read(1024*10) # 10kb
            if content == b'':
                break
            else:
                f2.write(content)
    return 1;

def copy_dir(source_dir, dest_dir):
    for f in os.listdir(source_dir):
        f_path = os.path.join(source_dir, f)
        if os.path.isfile(f_path) and f.endswith(('.py')):
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            dest_file = os.path.join(dest_dir, f)
            copy_single_file(f_path, dest_file)
        elif os.path.isdir(f_path):
            new_dir = os.path.join(dest_dir, f)
            copy_dir(f_path, new_dir)
        # dest_file = os.path.join(dest_dir, file)
        #     copy_single_file(full_path, dest_file)

def io_example():
    """
        mode:
        r: read mode, pointer at the beginning of file, by default
        rb: binary read mode, pointer at the beginning of file
        r+: read and write mode, pointer at the beginning of file
        rb+: binary read and write mode, pointer at the beginning of file
        w: write mode, pointer at the beginning of file, will remove original content, if file no exists, create new file
        wb: binary write mode, pointer at the beginning of file, will remove original content, if file no exists, create new file
        w+: read and write mode, pointer at the beginning of file, will remove original content, if file no exists, create new file
        wb+: binary read and write mode, pointer at the beginning of file, will remove original content, if file no exists, create new file
        a: append mode, pointer at the end of fil, new content will append original content, if file no exists, create new file
        ab: binary append mode, pointer at the end of fil, new content will append original content, if file no exists, create new file
        a+: read and write mode,  at the end of file, will remove original content, if file no exists, create new file
        ab+, binary read and write mode,  at the end of file, will remove original content, if file no exists, create new file
    """
    copy_dir("E:\Python_workspace\llm_learning\Python_basic\io_example1","E:\Python_workspace\llm_learning\Python_basic\io_example2");

if __name__ == '__main__':
    io_example()