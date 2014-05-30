# This is the main file of project - simply replace 'preamble.wav' with your desired wave file whose sampling you need to perform. 
#Note:wave file should be in same directory where mda.py resides
import numpy
from snd_io import read_wav_file, play
from primitives import *

from snd_utils import *
from numpy import *
import pylab

def main():
    data = read_wav_file('preamble.wav')
    slow = half_speed(data)

    dur = len(data)/float(SAMPLE_FREQUENCY)
    sine_data1 = sin_sample(440, .05, dur)
    sine_data2 = sin_sample(550, .05, dur)
    
    sine_data = combine_interleave([sine_data1, sine_data2])
    data = append(data, silence(dur))

    normalize(slow)
    data = combine_mean([sine_data, data, slow])
    data = echo(data, .3, .25)

    normalize(data)
    scale_volume(data, 1.2)

    play(data)
    view_wav(data,0,250)

if __name__ == '__main__':
    main()
