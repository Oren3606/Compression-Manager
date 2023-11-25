"""
api
"""

# imports

# todo: handle launch either from CLI or from GUI
mode = bool  # compress or uncompress
directory = str  # dir location
extension = str  # file type

wholefile = open('experimentation- file types/exe.exe', 'rb').read()
st = ''

for byte in wholefile:
    st += str(byte)
    print(byte, end=' ')
