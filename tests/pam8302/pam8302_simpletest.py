# Play .mp3 files from the Pico
import board
from audiomp3 import MP3Decoder
from audiopwmio import PWMAudioOut as AudioOut

# configure AudioOut & set path where sounds can be found
audio = AudioOut(board.GP14)
path = "sounds/"

filename = "levelcomplete.mp3"
mp3_file = open(path + filename, "rb")
decoder = MP3Decoder(mp3_file)

#decode.file = open(path + fn, "rb")
audio.play(decoder)
while audio.playing:
    pass # add code here that you want to run while sound plays


print("Done playing!")
