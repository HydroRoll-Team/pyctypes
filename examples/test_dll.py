#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from ctypes import cdll
from os.path import abspath, dirname, join

DIR = dirname(abspath(__file__))

def main():
    p = join(DIR, '..', 'x64', 'debug', 'PCH_H.dll')
    f = cdll.LoadLibrary(p)
    print(f.func(33))


if __name__ == '__main__':
    main()

