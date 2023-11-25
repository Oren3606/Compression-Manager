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


def uc_zip(file):
    # 1.  huffman coding
    from collections import defaultdict
    byte_freq = defaultdict()
    for byte in file.read():
        byte_freq[byte] += 1


def uc_rar(file):
    pass


def uc_jar(file):
    pass

def uc_iso(file):
    pass


def uc_tar(file):
    pass


def uc_gz(file):
    pass


def uc_7z(file):
    pass


def uc_apk(file):
    pass


def uc_dmg(file):
    pass


def uc_jar(file):
    pass


def uc_cab(file):
    pass


def uc_exe(file):
    pass
