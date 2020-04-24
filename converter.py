import os
from moviepy.editor import *

dirpath = str(input("Enter the target directory path(include '/' at the end): "))
pathlist = [vid for vid in os.listdir(dirpath)]

audiopath_prompt = str(input("Do you wish to use the same directory for the audiofiles? [Y/n]: "))
if audiopath_prompt == 'Y'.lower():
    audiopath = dirpath
elif audiopath_prompt == 'N'.lower():
    audiopath = str(input("Enter destination folder for the audio files('/' at the end): "))
else:
    print("Invalid entry.")

for vid in pathlist:
    vclip = VideoFileClip(os.path.join(dirpath, vid))
    audioclip = vclip.audio
    audioclip.write_audiofile('{}.mp3'.format(os.path.join(audiopath, vid.split('.mp4')[0]))) # Removing video extension to replace it with audio extension
