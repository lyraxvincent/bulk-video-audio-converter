import os
from moviepy.editor import *

dirpath = str(input("Enter the target directory path: "))
pathlist = [vid for vid in os.listdir(dirpath)]
fileFormats=["mp4", "mov", "wmv", "avi", "mkv", "webm"]     #Enter your video formats here
files=[]
for i in pathlist:
    try:
        if(i.split(".")[-1] in fileFormats):
            files.append(i)
    except:
        continue

audiopath_prompt = str(input("Do you wish to use the same directory for the audiofiles? [Y/n]: ")).upper()
if audiopath_prompt == 'Y':
    audiopath = dirpath
elif audiopath_prompt == 'N':
    audiopath = str(input("Enter destination folder for the audio files: "))
else:
    print("Invalid entry.")

for vid in files:
    vclip = VideoFileClip(os.path.join(dirpath, vid))
    audioclip = vclip.audio
    audioclip.write_audiofile('{}.mp3'.format(os.path.join(audiopath, ''.join(vid.split('.')[0:-1])))) # Removing video extension to replace it with audio extension
