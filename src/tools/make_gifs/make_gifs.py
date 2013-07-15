#!/usr/bin/env python
import logging
import sys
import os
import shutil
import subprocess

from videoconf import videoconf

###############################################################################
# Configure logging .. 
###############################################################################
# create logger
logger = logging.getLogger(os.path.basename(sys.argv[0]))
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

try:
    from subprocess import DEVNULL, DEVERR # py3k
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')
# uncomment this to get full output
#DEVNULL=None

def make_gif(filename):
    if filename not in videoconf:
        logger.error("no config found for file: '{0}'".format(filename))
        sys.exit(1)

    conf = videoconf[filename]
    
    logger.info("make GIF for '{0}'".format(filename))
    # init a temporary directory
    tmpdir = "tmp/_{0}_".format(filename)
    if (os.path.exists(tmpdir)):
        shutil.rmtree(tmpdir)
    os.makedirs(tmpdir) # mkdir -p 

    # extract / resize frames into PNGs with FFMpeg
    try:
        subprocess.check_call(['ffmpeg',
                              '-i' , filename, 
                              '-ss', conf['start'],
                              #'-t' , conf['length'],
                              '-s' , conf['size'],
                              '-f' , 'image2',
                              '{0}/%03d.png'.format(tmpdir)
                              ], stdout=DEVNULL, stderr=DEVNULL)

    except subprocess.CalledProcessError as e:
        logger.error(e)
        sys.exit(1)

    # prepare the list of frames to use for the GIF
    os.chdir(tmpdir)
    frames = os.listdir('.')
    frames = frames[::conf['subsample']]
     
    # do the GIF magic
    try:
        subprocess.check_call(['convert',
                               '-delay', conf['fps']
                              ] + 
                              frames +
                              ['-coalesce',
                               '-layers', 'OptimizeTransparency',
                               "../" + conf['output']
                              ], stdout=DEVNULL, stderr=DEVNULL)
        logger.info('output file created: {0}'.format("tmp/" + conf['output']))
        logger.info('check it out at: file:///' + os.path.abspath("../" + conf['output']))

    except subprocess.CalledProcessError as e:
        logger.error(e)
        sys.exit(1)

    os.chdir("../../")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        logger.info("make GIFs for all video files")
        for f in videoconf:
            make_gif(f)
    else:
        logger.info("make GIFs for {0}".format(sys.argv[1:]))
        for f in sys.argv[1:]:
            make_gif(f)
