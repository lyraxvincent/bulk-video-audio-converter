import os
from moviepy.editor import *

dirpath = str(input("Enter the target directory path: "))
pathlist = [vid for vid in os.listdir(dirpath)]
fileFormats=["mp4","mov","wmv","avi","mkv"]             #Enter your video formats here
files=[]
for i in pathlist:
    try:
        if(i.split(".")[-1] in fileFormats):
            files.append(i)
    except:
        continue
print(files)

audiopath_prompt = str(input("Do you wish to use the same directory for the audiofiles? [Y/n]: "))
if audiopath_prompt == 'Y' or audiopath_prompt == 'y':
    audiopath = dirpath
elif audiopath_prompt == 'N' or audiopath_prompt == 'n':
    audiopath = str(input("Enter destination folder for the audio files: "))
else:
    print("Invalid entry.")

for vid in files:
    vclip = VideoFileClip(os.path.join(dirpath, vid))
    audioclip = vclip.audio
    audioclip.write_audiofile('{}.mp3'.format(os.path.join(audiopath, vid.split('.')[0]))) # Removing video extension to replace it with audio extension
