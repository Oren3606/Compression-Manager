"""
api
"""
import builtins
# imports
# only if PACKING from os import path, scandir
from json import load

# todo: handle launch either from CLI or from GUI
# with open("settings.json") as settings_file:
#    settings = load(settings_file)
mode = bool  # compress or uncompress: True for compression, False for decompression
#directory = scandir(None)  # dir location, todo: get from launch

# todo: check all settings exist, else add defaults
# todo instead of this if block, import decode OR encode which will have corresponding imports?
if mode:
    from os import scandir


else:
    from tempfile import gettempdir as tmp_dir

s = scandir('experimentation- file types')
print(s)
for file in s:
    print(file.name)

wholefile = open('experimentation- file types/exe.exe', 'rb').read()
st = ''

# for byte in wholefile:
#   st += str(byte)
#  print(byte, end=' ')


"""
פותח קובץ
בתים מעובדים
קובץ נשמר בדירקטורי
פותח דירקטורי
אם דירקטורי נסגר, למחוק קובץ
לתת אפשרות לשמור את הקובץ בהורדות!!! 
"""
