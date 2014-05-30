digital-audio-sampler
=====================

A python project I did to perform digital audio analysis and sampling of a 22050 Hz audio wave file. The file is converted into samples using the pythn programs included.

All files have description included in them.
Complete set of audio and code files are at my google drive which can be found at:
Just run mda.py , provided you have a sample wave file of any frequency .

Project Description:
---------------------------------------------------------------------------------
 Any periodic analog signal can be decomposed into ( and also possible infinite ) number of sine waves ( the sum ) . However , a simple calculation can not express this function . Instead , sampling to obtain samples in discrete time intervals. Therefore , although not the original waveform , we can still get a lot of time waveform sample points . This is referred to as digital signals. Digital-analog converter according to reconstruct the original waveform sampling , and play with the speaker.
Sampling rate is called the sampling frequency. The unit is Hertz (Hz) or samples / second. The sample size is the number of digits used to represent each sample. The higher the sampling frequency high , the sample size , the higher the quality of the sound produced .
Analog to digital conversion (ADC) of the number of analog information as input and outputs a digital signal. When using a microphone , you might want to use such a device. When you speak into the microphone or play , your voice will cause the film to vibrate. It will be recorded many times per second in both directions of vibration  distance . These samples can be saved and used for playback . Naturally, the digital-analog conversion * (DAC) and the ADC is relative. DAC is sampled at a discrete time , and generates a continuous waveform. When using the mic you will find such a device. When you hear the sound on your computer, these discrete samples will be converted into a continuous signal can be played on the speakers .
In the case of certain conditions , the correct reconstruction of the analog signal by a digital signal is possible . When recording an analog signal , the most important thing is to know the maximum frequency that can be captured . This is the famous Nyquist frequency. Nyquist - Shannon theorem shows the error related to each dB level
The sampling frequency of the audio equipment most commonly used is 11025Hz, 22050Hz and 44100Hz. Maximum frequency because the human ear can hear is 20000Hz, so we should put maximum sampling frequency is set to 40000Hz. High sampling frequency and unnecessary and will only lead to more human beings can not hear the sound is sampled . Further , the sampling frequency , the greater the sound stored in the same interval of storage space required .
This project , we use the 22050Hz signal , which allows us to capture many samples audible domain. When you generate and input sound waves, to remember the number of samples per second is 22050 .
