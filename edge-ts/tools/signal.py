import numpy as np
import math

def genSine(f0, fs, dur):
    t = np.arange(dur)
    sinusoid = np.sin(2*np.pi*t*(f0/fs))
    sinusoid = normalise(sinusoid, MAX_INT16)
    return sinusoid

def genNoise(dur):
    noise = np.random.normal(0,1,dur)
    noise = normalise(noise, MAX_INT16)
    return noise

def normalise(x,MAX_INT16):
    maxamp = max(x)
    amp = math.floor(MAX_INT16/maxamp)
    norm = np.zeros(len(x))
    for i in range(len(x)):
        norm[i] = amp*x[i]
    return norm

def writeWav(w):
    print(w)

if __name__ == '__main__':
    f0 = 440
    fs = 16000
    dur = 1*fs                      #seconds
    MAX_INT16 = 32767
    sinusoid = genSine(f0,fs,dur)
    noise = genNoise(dur)
    sum = sinusoid + noise
    sum = normalise(sum,MAX_INT16)
    writeWav(sum)