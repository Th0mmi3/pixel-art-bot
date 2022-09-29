#from multiprocessing.reduction import duplicate
import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import os
import src.titles as titles
import random


t = titles.titler()

img_array = []

class vidMaker:
    def __init__(self):
        self.nTime = 12.97259375
        self.duplicateNum = 1

    def makeVidsFI(self):
        img_array = []

        for filename in os.listdir('src\\done'):
            useable = f'src\\done\\{filename}'
            img = cv2.imread(useable)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
            name = os.path.splitext(filename)[0]

            out = cv2.VideoWriter(f'src\\vidpart\\{name}.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 60, size)

            for x in range(120):
            
                out.write(img)

            out.release()
            videoNumber = len(os.listdir('src\\vidpart'))
            print(f"A vidpart has been generated ({videoNumber})")

    def checkPath(self, title):
        if os.path.exists(f'src\\output\\{title} #{self.duplicateNum}.mp4'):
            self.duplicateNum += 1

    def combVid(self, base, art, index):
        self.duplicateNum = 1
        output_name = 'src\\samples\\output.mp4'

        temp0 = 'src\\temp\\temp0.mp4'

        out = cv2.VideoWriter('src\\samples\\output2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 60, (1080, 1920))

        # Cut last part of video
        lF = self.nTime - VideoFileClip(base).end
        print(lF)
        clip = VideoFileClip(art)
        clip = clip.subclip(0, lF)
        clip.write_videofile(temp0)
        clip.close()

        # Extract block placing audio
        extracted_clip = VideoFileClip(base)
        extracted_clip.audio.write_audiofile("src\\temp\\temp1.mp3")
        extracted_audio = AudioFileClip("src\\temp\\temp1.mp3")

        # Combine both 
        clips = [base, temp0]

        for v in clips:
            curr_v = cv2.VideoCapture(v)
            while curr_v.isOpened():
                r, frame = curr_v.read()    # Get return value and curr frame of curr video
                if not r:
                    break
                #print(v)
                out.write(frame)          # Write the frame

        out.release()

        # Add audio
        audio_clip_music = AudioFileClip('src\\samples\\audio.mp3') # Music
        audio_clip_mc = AudioFileClip('src\\temp\\temp1.mp3') # Block placing audio
        audio_clip_music = audio_clip_music.subclip(0) # Don't know what this does

        audio_both = CompositeAudioClip([audio_clip_music, audio_clip_mc])

        video_clip = VideoFileClip('src\\samples\\output2.mp4')

        final_clip = video_clip.set_audio(audio_both) # Add audio to video


        output_title = t.create(index)

        self.checkPath(output_title)

        videoNumber = len(os.listdir('src\\output'))
        print(f"A video has been generated ({videoNumber})")
        final_clip.write_videofile(f'src\\output\\{output_title} #{self.duplicateNum}'+f'{random.randint(0,10000)}.mp4')


        
        

        



