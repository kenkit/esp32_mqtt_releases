#!/usr/bin/env python3

import platform
import sys
import ctypes
import lzss

if len(sys.argv) != 4:
    print ("Usage: lzss.py --[encode|decode] infile outfile")
    sys.exit()
mode   = sys.argv[1]
ifile  = sys.argv[2]
ofile  = sys.argv[3]

b_ifile = ifile.encode('utf-8')
b_ofile = ofile.encode('utf-8')

if mode == "--encode":
     lzss.encode_file.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
     lzss.encode_file(b_ifile, b_ofile)
elif mode == "--decode":
     lzss.decode_file.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
     lzss.decode_file(b_ifile, b_ofile)
else:
    print ("Error, invalid mode parameter, use --encode or --decode")
