# Play .mp3 files from the Pico
import os

import board
import busio
import sdcardio
import storage
# from audiomp3 import MP3Decoder
from audiopwmio import PWMAudioOut as AudioOut
from audiocore import WaveFile

# sdcard pins
sd_miso = board.GP12
sd_mosi = board.GP11
sd_sck = board.GP10
sd_cs = board.GP13

# Connect to the card and mount the filesystem.
spi = busio.SPI(sd_sck, MOSI=sd_mosi, MISO=sd_miso)
sdcard = sdcardio.SDCard(spi, sd_cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

def print_directory(path, tabs=0):
    for file in os.listdir(path):
        if file.startswith('.'):
            continue
        stats = os.stat(path + "/" + file)
        filesize = stats[6]
        isdir = stats[0] & 0x4000

        if filesize < 1000:
            sizestr = str(filesize) + " bytes"
        elif filesize < 1000000:
            sizestr = "%0.1f KB" % (filesize / 1000)
        else:
            sizestr = "%0.1f MB" % (filesize / 1000000)

        prettyprintname = ""
        for _ in range(tabs):
            prettyprintname += "   "
        prettyprintname += file
        if isdir:
            prettyprintname += "/"
        print("{0:<40} Size: {1:>10}".format(prettyprintname, sizestr))

        # recursively print directory contents
        if isdir:
            print_directory(path + "/" + file, tabs + 1)

filepath = "/sd/sounds"

print("Files on filesystem:")
print("====================")
print_directory(filepath)
print("====================")

# configure AudioOut & set path where sounds can be found
audio = AudioOut(board.GP14)

# single file play
# filename = "01_Running_About.wav"
# wave_file = open(path + "/" + filename, "rb")
# wave = WaveFile(wave_file)

# audio.play(wave)

# while audio.playing:
#     pass

def play_dir(path):
    print("start play_dir")
    # play multiple file
    for file in os.listdir(path):
        if file.startswith('.') or not file.endswith(".wav"):
            continue
        print("full path: [%s/%s]" % (path, file))
        wave_file = open(path + "/" + file, "rb")
        wave = WaveFile(wave_file)
        audio.play(wave)
        # wave.sample_rate = int(wave.sample_rate * 0.90) # play 10% slower each time
        print("Play [%s]" % file)
        while audio.playing:
            pass
        print("End Play")
        audio.stop()

try:
    play_dir(filepath)
except KeyboardInterrupt:
    audio.stop()
    print("audio player terminated.")
    
print("Done playing!")
