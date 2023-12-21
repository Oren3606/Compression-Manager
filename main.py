"""
api
"""

# imports
from os import path, scandir
from json import load

# todo: handle launch either from CLI or from GUI
# with open("settings.json") as settings_file:
#    settings = load(settings_file)
mode = bool  # compress or uncompress: True for compression, False for decompression
directory = scandir(None)  # dir location, todo: get from launch

if mode:
    from os import scandir

else:
    pass

s = scandir('experimentation- file types')
print(s)
# if not mode:
for file in s:
    print(file.name)

wholefile = open('experimentation- file types/exe.exe', 'rb').read()
st = ''

# for byte in wholefile:
#   st += str(byte)
#  print(byte, end=' ')
