"""
default compression parameters:
zip:
rar:
jar:
iso:
tar:
gz:
7z:
apk:
"""


def zip(file):
    # 1.  huffman coding
    from collections import defaultdict
    byte_freq = defaultdict()
    for byte in file.read():
        byte_freq[byte] += 1


def rar(file):
    pass


def jar(file):
    pass


def iso(file):
    pass


def tar(file):
    pass


def gz(file):
    pass


def seven_z(file):
    pass


def exe(file):
    pass
