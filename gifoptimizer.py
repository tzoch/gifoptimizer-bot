#! /usr/bin/python

import subprocess
import os

import PythonMagick

target_im = 'example_images/gta_original.gif'
#im = PythonMagick.Image(target_im)

extract_frames = ['convert', '-coalesce', '+adjoin', 
                   target_im, 'tmp/%03d.png']

recombine_frames = ['convert', '-resize', '75%', '-fuzz', '2%', '-loop',
                    '0', 'tmp/*.png', '-layers', 'OptimizePlus', '-layers', 
                    'OptimizeTransparency', 'tmp.gif']

reduce_colors = ['gifsicle', '-O3', '--colors', '128', '-d4', 'tmp.gif', 
                 '-o', 'final.gif']

subprocess.call(extract_frames)
subprocess.call(recombine_frames)
subprocess.call(reduce_colors)
