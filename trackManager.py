from pydub import AudioSegment
from glob import glob

AudioSegment.converter = r"ffmpeg.exe"

def loadMP3(path):
    return AudioSegment.from_file(path, format="mp3")

def loadPlaylist(path):
    return [(AudioSegment.from_mp3(track), track, '.'.join(track.split('\\')[-1].split('.')[:-1])) for track in glob(path + "/*.mp3")] #(AudioSegment, path, name)

#currently only one overlay and first five seconds of track for testing
def mergeVoiceover(track, voiceover, times):
    if(times == 0):
        print('Not implemented yet, switch to 1')
        overlay(track, voiceover, 1)
    elif(times == 1):
        print('Merge at the beginning')
        return track.overlay(voiceover, position=100, gain_during_overlay=-12)
    elif(times < 11):
        #calculate voiceover startpoints
        trackLength = len(track)
        interval = trackLength/times
        print('Tracklength: ', trackLength)
        print('Interval: ', interval)
        iterator = 0
        for i in range(times):
            track = track.overlay(voiceover, position=iterator, gain_during_overlay=-10)
            iterator += interval
        print('Merged ', times, ' times.')
        return track
    else:
        print('Invalid Input at: trackManager: overlay. Only numbers between 0 and 10 are allowed.')

def saveMP3(track, path):
    track.export(path, format="mp3")
    print('Track saved.')