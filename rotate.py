#!/usr/bin/env python3
import argparse
import subprocess

def rotate(rotation):
    if rotation == 'default':
        command = 'fb-rotate -d 1 -r 0'.split()
        subprocess.call(command)
    elif rotation == 'clockwise' or rotation == 'right':
        command = 'fb-rotate -d 1 -r 270'.split()
        subprocess.call(command)
    elif rotation == 'counterclockwise' or rotation == 'left':
        command = 'fb-rotate -d 1 -r 90'.split()
        subprocess.call(command)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('rotation',
                        choices=['clockwise', 'counterclockwise',
                                 'right', 'left', 'default'])
    args = parser.parse_args()
    
    rotate(args.rotation)
