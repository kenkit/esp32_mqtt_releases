#!/usr/bin/env python3

import sys
import lzss

if len(sys.argv) != 4:
    print ("Usage: lzss.py --[encode|decode] infile outfile")
    sys.exit()

mode   = sys.argv[1]
ifile  = sys.argv[2]
ofile  = sys.argv[3]

with open(ifile, 'rb') as f_in:
    data = f_in.read()

if mode == "--encode":
    processed_data =  lzss.compress(data)
elif mode == "--decode":
    processed_data =  lzss.decompress(data)
else:
    print ("Error, invalid mode parameter, use --encode or --decode")
    sys.exit(1)

with open(ofile, 'wb') as f_out:
    f_out.write(processed_data)

