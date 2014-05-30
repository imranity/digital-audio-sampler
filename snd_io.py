# Basic functions for dealing file I/O with wave files
########################################################################
# This file is provided to assist in the completion of the course      #
# audio project. You should have a good idea of what is happening here #
# but are not required to understand all aspects of the code.          #
########################################################################

import wave
import os,sys

import cStringIO        # Faster version of StringIO (for binary strings)
import struct           # For raw string I/O
import time             # For sleep()
import audioop
from numpy import array,append,zeros,empty # get array type
import numpy
import math

SAMPLE_RATE = 22050     # Handle samples @ 22050 Hz
N_CHANNELS = 1          # Monoaural
SAMPLE_WIDTH = 2        # 16-bit ( = 2 byte) WAV samples

def read_wav_file(name):
    """
    This function reads a WAV file named 'name' and returns
    an array containing integral samples.
    """

    # Open wave file for reading
    w = wave.open(name, 'rb')
    nchannels = w.getnchannels()

    # Read the wave as a raw string. Caution, this could use a
    # lot of memory!
    raw = w.readframes(w.getnframes())

    # Convert to a list of samples
    # Mono
    if nchannels == 1:
        data = empty(w.getnframes(), dtype=numpy.int16)
        for i in xrange(0, w.getnframes()):
            data[i] = audioop.getsample(raw,w.getsampwidth(),i)
    elif nchannels == 2:
        data = empty(2*w.getnframes(), dtype=numpy.int16)
        for i in xrange(0, w.getnframes()):
            data[i] = audioop.getsample(raw,w.getsampwidth(),i)

        data = array([data[0::2],data[1::2]], dtype=numpy.int16)
    return data

def save_wav_file(name, data):
    """
    Save the output as a wave file with name containing data.
    """
    
    w = wave.open(name, 'wb')
    w.setnchannels(data.ndim)
    w.setsampwidth(SAMPLE_WIDTH)
    w.setframerate(SAMPLE_RATE)

    # Might want to make this more efficient later
    if data.ndim == 2:
        data = array(zip(data[0],data[1]), dtype=numpy.int16).flat
        w.setnframes(len(data)/2)
    else:
        w.setnframes(len(data))

    w.writeframesraw(pack(data))
    w.close()
    
def unpack(data):
    """
    This function extracts a raw byte string into an array of
    16-bit integers.
    """
    undata = empty(len(data)/2, dtype=numpy.int16)
    for i in xrange(0, len(data)/SAMPLE_WIDTH):
        undata[i] = audioop.getsample(data,SAMPLE_WIDTH,N_CHANNELS)

def pack(data):
    """
    Pack a list of wav samples back into a string for audio
    output. This function returns the raw data as a string.
    """

    sio = cStringIO.StringIO() # For storing packed string

    for d in data:
        sio.write(struct.pack('h',d))

    return sio.getvalue()

def play(data):
    """
    For now, play() dumps a temporary file in the CWD.
    """
    fileno = 0
    name = './temp-%04d.wav' % (fileno,)

    while os.path.exists(name):
        fileno += 1
        name = './temp-%04d.wav' % (fileno,)

    save_wav_file(name, data)

    print 'Wrote output to', name

if __name__ == '__main__':
    sys.stderr.write('This module is provided to handle sound I/O and does ' +
                     'not contain any independently executable code!\n')
    sys.exit(1)
