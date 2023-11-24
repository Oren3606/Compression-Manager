"""
api
"""

# imports

# todo: handle launch either from CLI or from GUI
mode = bool #compress or uncompress
directory = str # dir location
type = str # file type

with open('elevator.exe', 'rb') as p_file:
    content = p_file.read()
    print(type(content[1]))
  #  bin = ''
  #  print(content)
  #  for ch in content:
 #       while ch>8:
  #          bin+='1'
  #          ch-=8
  #      bin += ord(ch)

    print(bin)
    # while (content):  # if there are still bytes to iterate through
    #   cur_byte = content[0:8]
    #  for i in range(0, 8):
    #     pass
