import GUIStart
import OCR
import pytesseract
import SummarizationRun
import SplitToTinyVideos
import BuildNewVideo
if __name__=='__main__':
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\324868629\Desktop\Project\Codalleh-AnyClip\OCREngine\tesseract.exe"
    video_path=GUIStart.create_app()
    path_csv=OCR.OCRFunction(video_path)
    path_csv=SummarizationRun.summarizationFunction(path_csv)
    directory_videos=SplitToTinyVideos.tinyVideosFunction(video_path,path_csv)
    BuildNewVideo.buildVideoFunction(video_path,directory_videos)