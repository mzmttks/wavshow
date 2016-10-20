import sys

import numpy
import soundfile
import matplotlib.pyplot as plt


def plotwav(wav, fs):
  plt.plot(wav, "k-")
 
  xticks, strs = plt.xticks()
  plt.xticks(xticks, ["%.2f" % (x/fs) for x in xticks])

  plt.ylim(-1, 1)
  plt.xlim(0, len(wav))
  plt.xlabel("Time [s]")
  plt.ylabel("Amplitude")

if __name__ == "__main__":
  wavname = sys.argv[1]

  obj = soundfile.SoundFile(wavname)
  wav = obj.read()
  fs = obj.samplerate

  is_multichannel = len(wav.shape) == 2

  if is_multichannel:
    plt.subplot(wav.shape[1], 1, 1)
    plt.title(wavname)

    for ch in range(wav.shape[1]):
      plt.subplot(wav.shape[1], 1, ch+1)
      plotwav(wav[:, ch], fs)
  else:
    plt.title(wavname)
    plotwav(wav, fs)

  plt.show()
  print is_multichannel
  print wav.shape
