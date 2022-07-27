from moviepy.video.io.VideoFileClip import VideoFileClip
import pandas as pd


def tinyVideosFunction(video_path,path_csv):
    input_video_path = video_path
    video_path = r"C:\Users\324868629\Desktop\Project updated\Codalleh-AnyClip\AnyClipDataSet\SummarizationModel\partsOfVideo"
    times_file=pd.read_csv(path_csv)
    data = pd.DataFrame(times_file)


    with VideoFileClip(input_video_path) as video:

        for i in range(data.index.stop):
            new = video.subclip(data.startTime[i], data.endTime[i])
            output_video_path=video_path+"\\"+str(i)+".mp4"
            new.write_videofile(output_video_path)
    return video_path

