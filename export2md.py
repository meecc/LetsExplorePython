# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 06:19:01 2017

@author: johri_m
"""

import os
import subprocess
import shutil
from optparse import OptionParser


def execute(cmd):
    """Execute.

    Purpose  : To execute a command and return exit status
    Argument : cmd - command to execute
    Return   : exit_code
    """
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    (result, error) = process.communicate()

    rc = process.wait()

    if rc != 0:
        print("Error: failed to execute command:", cmd)
        print(error)
    return result


htmlFiles = []
parser = OptionParser()
parser.add_option("-s", "--source", dest="source",
                  help="parent source directory", metavar="source")
parser.add_option("-d", "--dest", dest="dest",
                  help="destination directory")

(options, args) = parser.parse_args()
print(options)

for d in os.walk(options.source):
    for f in d[2]:
        if f.endswith(".ipynb") and "-checkpoint" not in f:
            print("Processing: ", f)
            file_name = os.path.join(d[0], f)
            execute("jupyter nbconvert --to Markdown \"" + file_name + "\"")
            file_name_md = os.path.splitext(file_name)[0] + ".md"
            htmlFiles.append(os.path.abspath(file_name_md))

cwd = os.getcwd()
dest = options.dest
print("options.dest" + dest)
for f in htmlFiles:
    print("Copying file:", f)
    d = os.path.split(f.split(cwd)[1])[0][1:]
    dest_path = os.path.join(dest, d)
    print("path", dest_path)
    os.makedirs(dest_path, exist_ok=True)
    shutil.copy(f, dest_path)
