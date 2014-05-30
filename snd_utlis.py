#simple program to assist in displaying better formatted data for audio files 
########################################################################
# This file is provided to assist in the completion of the course      #
# audio project. You should have a good idea of what is happening here #
# but are not required to understand all aspects of the code.          #
########################################################################

from pylab import *

def view_wav(data, start, nsamples):
    if data.ndim == 1:
        grid()
        xlabel('Sample #')
        ylabel('Sample value')
        title('Wave data from sample ' + str(start) +
          ' to ' + str(start + nsamples))
        plot(range(start, start+nsamples), data[start:(start+nsamples)], 'r',
             lw=1.5)
        show()
        #savefig('figure1.png')
    elif data.ndim == 2:
        subplot(211)
        grid()
        xlabel('Sample #')
        ylabel('Sample value')
        title('Wave data from sample ' + str(start) +
          ' to ' + str(start + nsamples) + ' (Left)')
        plot(range(start, start+nsamples), data[0][start:(start+nsamples)], 'r',
             lw=1.5)
        subplot(212)
        grid()
        xlabel('Sample #')
        ylabel('Sample value')
        title('Wave data from sample ' + str(start) +
          ' to ' + str(start + nsamples) + ' (Right)')
        plot(range(start, start+nsamples), data[1][start:(start+nsamples)], 'r',
             lw=1.5)
        show()
        #savefig('figure2.png')
