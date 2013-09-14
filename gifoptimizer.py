#! /usr/bin/python

import subprocess

import PythonMagick

im = PythonMagick.Image("example_images/plane_original.gif")

print im.fileName()
print im.magick()
print im.size().width()
print im.size().height()
print dir(im.format())
