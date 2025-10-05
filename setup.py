"""
Installs everything necessary for this package

On linux: install minimal clang compiler from google drive

On windows: install minimal mingw64 compiler from google drive
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[0])) 
sys.path.append(str(Path(__file__).resolve().parents[1])) 
sys.path.append(str(Path(__file__).resolve().parents[2])) 
sys.path.append(str(Path(__file__).resolve().parents[3])) 
sys.path.append(str(Path(__file__).resolve().parents[4])) 

from vicmil_pip.lib.pyUtil import *
from vicmil_pip.installer import install_package

import zipfile

def get_compiler_path():
    if platform.system() == "Windows":
        return get_directory_path(__file__, 1) + "/mingw64/mingw64/bin/g++.exe"
    if platform.system() == "Linux":
        return get_directory_path(__file__, 1) + "/gcc13_2_0/gcc-13.2.0/gcc-13.2.0/bin/g++"
    

def get_output_file_extension():
    if platform.system() == "Windows":
        return ".exe"
    if platform.system() == "Linux":
        return ".out"
    

def add_env_paths_to_compiler():
    if platform.system() == "Linux":
        compiler_path = get_directory_path(__file__, 1) + "/gcc13_2_0/gcc-13.2.0"
        
        os.environ["PATH"] = f"{compiler_path}/gcc-13.2.0/bin:{compiler_path}/gcc-13.2.0/libexec/gcc/x86_64-pc-linux-gnu/13.2.0:" + os.environ["PATH"]
        os.environ["GCC_EXEC_PREFIX"] = f"{compiler_path}/gcc-13.2.0/lib/gcc/"
    

def install():
    if platform.system() == "Windows":
        install_package("mingw64")

    if platform.system() == "Linux":
        install_package("gcc13_2_0")


if __name__ == "__main__":
    install()