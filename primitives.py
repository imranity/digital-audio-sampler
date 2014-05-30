#primitives.py file provides all 8 basic primitvves related to sampling- such as scaling, maxima etc

# Project 
# this file gives templates for the eight audio primitives (part 1) and
# the functions that can be used as the optimal one (hand in with part 2)
# 

import numpy
import math
from numpy import zeros, empty, array, append

# Helpful constants
WAVE_MAX = 32767            # Max sample value
WAVE_MIN = -32768           # Min sample value
SAMPLE_FREQUENCY = 22050    # Sampling frequency in Hz

from snd_io import read_wav_file, save_wav_file, play
#########
#
# Summary of function usage:
#
# read_wav_file(name)
#   Reads a WAV file stored in a file named by name. This should be a
#   22050Hz Mono WAV.
#
# save_wav_file(name, data)
#   Saves a WAV file to a file named by name and containing 'data'.
#   data should be an array of 16 bit integers representing samples
#   at 22050Hz.
#
# play(data)
#   Play samples stored in 'data'. If the supporting moudles for sound
#   are not present. this will dump a file named "temp.wav" to the
#   current working directory.
#
#########

########################################################################
#
# Required functions skeletons
#
# submit the eight required function is a file named primitives.py 
#
########################################################################

def scale_volume(data, factor):
    """
    scale_volume(data, factor)

    This function takes samples specified in data and scales them all
    by a constant factor. To accomplish this, every element of the data
    array is multiplied by a constant factor which will correspondingly
    increase or decrease the volume of the wave (corresponding to factors
    greater than 1 or less than 1 respectively). Note that this may result
    int samples that are out of range. The following actions are taken:

    - If a scaled sample is greater than WAVE_MAX, set it to WAVE_MAX
    - If a scaled sample is less than WAVE_MIN, set it to WAVE_MIN

    This will result in clipping.
    Take care to note that factor may be a floating point value
    (e.g. 0.5) so attention must directed to making sure the result
    of the scaling is an integer. This may be accomplished as follows:
 
      x = 3.5
      print x,int(x)
 
    prints:
 
      3.5 3
 
    Note that all decimal places are TRUNCATED.
    """
    # Scale each sample by factor
    k = 0
    for val in data:
        adjusted = int(factor*val)
 
        # Make sure we're not scaling to an invalid value
        if adjusted > WAVE_MAX:
            adjusted = WAVE_MAX
        elif adjusted < WAVE_MIN:
            adjusted = WAVE_MIN
 
        data[k] = adjusted
        k += 1
    return


########################################################################

def normalize(data):
    """
    normalize(data)

    This function maximizes the possible volume of a wave by ensuring that
    the maximum possible sample scaling is used. In principle this is similar
    to the scale_volume() function except that the scaled values are
    maximized and should always be in range. Because of this it is safe to
    use the array operations.

    The following functions may be helpful:

       max(a) - returns the laegest element of a
       min(a) - returns the smallest element of a
       abs(x) - returns the absolute value of x

    Note the special case where all samples are 0.
    """
    largest = max(data)
    smallest = min(data)
    scale_factor = 0
 
    if largest != 0 or smallest != 0:
        if largest >= abs(smallest):
            scale_factor = WAVE_MAX/largest
        else:
            scale_factor = WAVE_MAX/abs(smallest)
 
    for k in range(len(data)):
        data[k] = int(scale_factor * data[k])
    return

########################################################################

def echo(data, delay, level):
    """
    echo(data, delay, level)

    This function takes an array of samples, a delay in seconds,
    and an echo level.

    Remember that the delay is in seconds, and the value must be
    translated to have a meaning in terms of actual sampling.
    The SAMPLE_FREQUENCY value indicates the number of samples/sec.

    The level should be between 0 and 1. The level indicates the intensity
    of the echo in proportion to the original sound. Correspondingly, the
    original wave will scaled by a factor of (1 - level).

    To create an echo effect, the sound is shifted by a certain number of
    samples. The pieces of the waves that do not overlap are matched by
    silence in the other wave. For each sample, the result is the weighted
    average:
    
      result = (1-level)*orig_sample + level*echo_sample

    NOTE: Since the resulting array is not the same size as the input array,
    this function returns a new array containing the result. Also, remember
    that delay may be a floating point number, so it is important to make
    sure that when calculating the number of samples in the delay that the
    result is an integer.
    """
        
    delay_samples = int(delay*SAMPLE_FREQUENCY)
    z = zeros(delay_samples)
    orig_data=append(data,z)
    echo_data=append(z,data)
    output = empty(len(orig_data), dtype=numpy.int16)

    for k in xrange(0,len(orig_data)):
        out = (1 - level)*orig_data[k] + level*echo_data[k]
        if out > WAVE_MAX:
            out = WAVE_MAX
        elif out < WAVE_MIN:
            out = WAVE_MIN
 
        output[k] = out

    # Echo generation goes here

    return output

########################################################################


def sin_sample(freq, amp, dur):
    """
    sin_sample(freq, amp, dur)
    
    This function returns a sine wave with frequencey freq, amplitude amp,
    and duration dur (in seconds). The smplitude should be specified
    with a range of 0 to 1 where 1 represents the maximal amplitude.

    To obtain the actual amplitude in the sample use the WAVE_MAX value
    to scale it to an appropriate value.
    """        
    output = empty(int(dur*SAMPLE_FREQUENCY), dtype=numpy.int16)
    factor = WAVE_MAX*amp
 
    for t in xrange(0,len(output)):
        output[t] = factor*math.sin(2*math.pi/SAMPLE_FREQUENCY*freq*t)

    return output


########################################################################


def combine_mean(wavs):
    """
    This function takes a list of data from different wave samples and
    combines them into a single sound. All samples must have the same
    length.

    Recall that in python *wavs means the functions takes a variable
    number of arguments. The arguments are packed into a tuple, which
    can be iterated similarly to a list or array.

    To calculate the combined wave, take the sum of each wave sample
    divided by thenumber of wave samples (i.e. the mean).
    """
       
    output = zeros(len(wavs[0]), dtype=numpy.int16)
    
    for a in wavs:
        output += (a/len(wavs))
 
    return output

########################################################################


def silence(dur):
    """
    silence(dur)

    Return a sample with dur seconds of silence
    """
        
    return zeros(int(dur*SAMPLE_FREQUENCY), dtype=numpy.int16)

########################################################################


def half_speed(data):
    """
    This function takes an array of data and repeats each sample twice.
    The result is that the original sound is effectively half the speed
    of the original when played.

    That is:

    [x1,x2,x3,x4] =&gt; [x1,x1,x2,x2,x3,x3,x4,x4]
    """
    result = empty(len(data)*2, dtype=numpy.int16)
    for k in xrange(len(data)):
        result[2*k] = data[k]
        result[2*k+1] = data[k]
 
    # Or we could cheat and just return data.repeat(2) ;-)
    return result


########################################################################


def combine_interleave(wavs):
    """
    This function takes a list of waves that may have different lengths.
    The resulting wave takes samples from the waves and interleaves them.

    The resulting wave's length is equal to the length of the shortest
    wave multiplied by the number of waves.  That is, the waves are only
    interleaved so long as there are more samples left in all waves.

    For example:

    [[x1,x2,x3,x4], [y1,y2,y3], [z1,z2,z3,z4,z5]] =&gt;
        [x1,y1,z1,x2,y2,z2,x3,y3,z3]

    Because of the discontinuity this introduces into the waves, it is
    normal to hear some high frequency noise. Also, when mixing more
    than two waves in this way, the result will not resemble any of the
    inputs very much.
    """
    length = len(wavs[0])
    for w in wavs:
        length = min(length,len(w))
        
    result = empty(len(wavs)*length, dtype=numpy.int16)

    for k in xrange(length):
        for l in xrange(len(wavs)):
            result[len(wavs)*k+l] = wavs[l][k]

    return result

# See examples for usage examples
if __name__ == '__main__':
    pass
