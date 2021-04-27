import pydub
from pydub import AudioSegment
from pydub.playback import play

AudioSegment.converter = r"ffmpeg.exe"

track = AudioSegment.from_file('tracklists/lab/5vel - RainOnMe.mp3', format='mp3')
voiceover = AudioSegment.from_file('voiceover.mp3', format='mp3')
overlayed = track[:5000].overlay(voiceover)
overlayed.export("result.mp3", format="mp3")