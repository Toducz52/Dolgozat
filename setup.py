import os
import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

include_files = [r'C:\Users\ToduczEndre\PycharmProjects\pythonProject2\db\example.db',
                 r'C:\Users\ToduczEndre\PycharmProjects\pythonProject2\builder_method\qt_designer.ui']

includes = []

build_exe_options = {"includes": includes, "include_files": include_files}

setup(
    name='Autoexport',
    version='1.0',
    description='auto export for matrix tool',
    options={"build_exe": build_exe_options},
    executables=[Executable(r'C:\Users\ToduczEndre\PycharmProjects\pythonProject2\main.py')]
)
