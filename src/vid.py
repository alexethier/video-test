#!/usr/bin/env python
from __future__ import unicode_literals
import argparse
import ffmpeg
import sys
import logging
import os


parser = argparse.ArgumentParser(
    description='Read individual video frame into memory as jpeg and write to stdout')
parser.add_argument('in_filename', help='Input filename')
parser.add_argument('frame_num', help='Frame number')

LOGGER = logging.getLogger(__name__)

def test_eggs():
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    LOGGER.critical('eggs critical')

def run_process():
    LOGGER.info("hi")
    #cwd = os.getcwd()
    #LOGGER.info("Scanning " + cwd + " for .mpeg file")
    #for root, dir, files in os.walk(cwd):
    #    LOGGER.info(root)
    #    LOGGER.info("")
    #    for items in fnmatch.filter(files, "*"):
    #            LOGGER.info("..." + items)
    #    LOGGER.info("")

def read_frame_as_jpeg(in_filename, frame_num):
    out, err = (
        ffmpeg
        .input(in_filename)
        .filter('select', 'gte(n,{})'.format(frame_num))
        .output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
        .run(capture_stdout=True)
    )
    return out


if __name__ == '__main__':
    test_eggs()
    #args = parser.parse_args()
    #out = read_frame_as_jpeg(args.in_filename, args.frame_num)
    #sys.stdout.buffer.write(out)
