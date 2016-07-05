#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2016-07-05 21:03:02

from PIL import Image
import os
import sys


def png2coe(imageName):
    """
    Transfer from png to coe

    :imageName: TODO
    :returns: TODO

    """
    im = Image.open(imageName)
    width = im.size[0]
    height = im.size[1]
    forward,end = os.path.splitext(imageName)
    outfile = forward + ".coe"
    with open(outfile,'w') as f:
        f.write('MEMORY_INITIALIZATION_RADIX=2;\n')
        f.write('MEMORY_INITIALIZATION_VECTOR=\n')
        for h in range(height):
            for w in range(width):
                pixel = im.getpixel((w,h))
                if pixel[3] <= 100:
                    f.write('{:0>8b}{:0>8b}{:0>8b},\n'.format(255,255,204))
                else:
                    if pixel == [255,255,204]:
                        f.write('{:0>8b}{:0>8b}{:0>8b},\n'.format(pixel[0],pixel[1],pixel[2]+1))
                    else:
                        f.write('{:0>8b}{:0>8b}{:0>8b},\n'.format(pixel[0],pixel[1],pixel[2]))


if __name__ == '__main__':
    ImageName = sys.argv[1]
    png2coe(ImageName)

