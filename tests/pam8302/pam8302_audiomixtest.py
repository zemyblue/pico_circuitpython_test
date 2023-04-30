# Play .mp3 files from the Pico
import board
import time
import audiomixer
from audiopwmio import PWMAudioOut as AudioOut
from audiocore import WaveFile


# configure AudioOut & set path where sounds can be found
audio = AudioOut(board.GP14)
path = "sounds/"

# warning: The all sound file should be same sample_rate and same bits_per_sample.
music_filename = "music.wav"
effect_files = ("1.wav", "2.wav")

mixer = audiomixer.Mixer(voice_count=2, 
                         sample_rate=22050, 
                         channel_count=1, 
                         bits_per_sample=16, 
                         samples_signed=True)

effect_idx = 0

try:
    print("Playing")
    audio.play(mixer)
    # play background
    music = WaveFile(open(path + music_filename, "rb"))
    mixer.voice[0].play(music, loop=True)
    while mixer.playing:
        # play effect sound
        print("effect sound idx: %d" % effect_idx)
        effect = WaveFile(open(path + effect_files[effect_idx], "rb"))
        mixer.voice[1].play(effect)
        effect_idx = (effect_idx + 1) % 2
        time.sleep(1)
except Exception as err:
    audio.stop()
    print(f"audio player terminated. {err=}")

print("Done playing!")
