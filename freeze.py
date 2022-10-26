#!/usr/bin/python3
# Copyright 2022 fnwinter@gmail.com

import subprocess

PACKAGE_NAME_SELF = 'py_template_daemon'

def freeze():
  requirements = subprocess.run(['pip', 'freeze'],\
    capture_output=True,\
    text=True).stdout.splitlines()
  del_self_package = list(filter(lambda x: not PACKAGE_NAME_SELF in x, requirements))
  
  with open('requirements.txt', 'w') as f:
    f.write("\r\n".join(del_self_package))

  with open('requirements.py', 'w') as f:
    f.write("req = [\r\n")
    for req in del_self_package:
      if PACKAGE_NAME_SELF in req:
        continue
      f.write(f"  '{req}',\r\n")
    f.write("]\r\n")
  print("done")

if __name__ == '__main__':
  freeze()
