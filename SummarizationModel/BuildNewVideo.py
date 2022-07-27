from moviepy.editor import *
import os
from natsort import natsorted


def buildVideoFunction(video_path,directory_videos):
    L =[]
    for root, dirs, files in os.walk(directory_videos):

        files = natsorted(files)
        for file in files:
            if os.path.splitext(file)[1] == '.mp4':
                filePath = os.path.join(root, file)
                video = VideoFileClip(filePath)
                L.append(video)

    final_clip = concatenate_videoclips(L)
    find_index=video_path.rfind('/')
    cut_string=video_path[:find_index+1]
    path_to_output_video=cut_string+"output.mp4"
    final_clip.to_videofile(path_to_output_video, fps=24, remove_temp=False)


