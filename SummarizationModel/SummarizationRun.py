from transformers import pipeline
import difflib
from difflib import *
import pandas as pd
import csv


def summarizationFunction(path_to_csv):
    path=path_to_csv
    csv_file = pd.read_csv(path, error_bad_lines=False)
    data = pd.DataFrame(csv_file)

    classifier = pipeline("summarization")
    whole_text=""
    whole_arr=[]

    for i in range(data.index.stop):

        current_sentence=data.data[i]
        whole_arr.append(current_sentence)
        whole_text+=current_sentence


    summary_text=classifier(whole_text)

    summary_text=summary_text[0]["summary_text"]
    summary_arr=summary_text.split(".")

    with open(r"C:\Users\324868629\Desktop\Project updated\Codalleh-AnyClip\AnyClipDataSet\SummarizationModel\whole.txt","w")as fp:
        for item in whole_arr:
            fp.write("%s\n"% item)

        fp.close()

    with open(r"C:\Users\324868629\Desktop\Project updated\Codalleh-AnyClip\AnyClipDataSet\SummarizationModel\summerized.txt","w")as sp:
        for item in summary_arr:
            sp.write("%s\n" % item)
        sp.close()


    with open(r"C:\Users\324868629\Desktop\Project updated\Codalleh-AnyClip\AnyClipDataSet\SummarizationModel\whole.txt") as f, open(r"C:\Users\324868629\Desktop\Project updated\Codalleh-AnyClip\AnyClipDataSet\SummarizationModel\summerized.txt") as g:
        whole_lines = f.readlines()
        summary_lines = g.readlines()
        d = difflib.Differ()
        diff = d.compare(whole_lines, summary_lines)


    time_dict={}

    with open (r"C:\Users\324868629\Desktop\Project updated\Codalleh-AnyClip\OCR\video_data.csv", "r") as file:
        reader=csv.DictReader(file,skipinitialspace=True)

        i=0
        for line in reader:

           sentence_from_orginal=line["data"].strip().lower()
           sentence_from_summary=summary_lines[i].strip().lower()
           if   sentence_from_summary in sentence_from_orginal :
               arr_time = []
               arr_time.append(line["startTime"])
               arr_time.append(line["endTime"])
               time_dict[i]=arr_time
               i+=1
           else:
               continue


    df=pd.DataFrame(time_dict,index=['startTime','endTime']).T
    path_of_csv=r"C:\Users\324868629\Desktop\Project updated\Codalleh-AnyClip\AnyClipDataSet\SummarizationModel\frames_to_build_video.csv"
    df.to_csv(path_of_csv)
    return path_of_csv

