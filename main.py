import pydub
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
from glob import glob
import os
import sys

import voiceover as vo
import trackManager as tm

if(len(sys.argv) != 2):
    print('Invalid number of arguments. Please enter the playlist foldername in tracklist folder as only argument')
    exit()
elif(sys.argv[1] == 'tracklists'):
    print('Invalid Tracklist name. Choose another name')
    exit()

path_dir = "tracklists/"
source_foldername = sys.argv[1]
source_dir = path_dir + source_foldername
playlist_tracks = tm.loadPlaylist(source_dir)
print(playlist_tracks)

target_dir = path_dir + source_foldername + "_res"
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

for track in playlist_tracks:
    target_path = target_dir + '/' + track[2] + '.mp3'
    vo.createVoiceover(track[2], target_path)
    voiceover = tm.loadMP3(target_path)
    track_result = tm.mergeVoiceover(track[0], voiceover, 4) #hardcoded number of voiceovers
    tm.saveMP3(track_result, target_path)
    
print('done.')