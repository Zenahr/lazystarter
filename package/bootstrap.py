# -*- coding: utf-8 -*-


"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.1.0"


import sys
from .sub_module import Main


def main():
    print()
    print("lazystarter version %s." % __version__ + " invoked")
    print("Passed arguments: %s" % sys.argv[1:])
    print("sub module:", Main)