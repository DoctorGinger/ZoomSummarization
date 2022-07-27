from datasets import load_dataset
import os
#dataSet=load_dataset(r"C:\Users\324868629\Desktop\Project\Codalleh-AnyClip\AnyClipDataSet\anyClipDataSet")

data_dir=r"C:\Users\324868629\Desktop\Project\Codalleh-AnyClip\AnyClipDataSet\origin\Highlights_examples"

all_files = os.listdir(os.path.abspath(data_dir))
data_files = list(filter(lambda file: file.endswith('.txt'), all_files))

new=[]
#all_sentences=[]
for i in data_files:
    completeName = os.path.join(data_dir ,i)
    #print(completeName)
    file = open(completeName,"r+")
    print(file)
    #file = open(completeName, "w")
    s=file.read()
    new=s.split('\n')
    file.truncate(0)
    # s=file.read()
    # s.lstrip()
    # file.write(s)
    for j in new:
        j=j[20:]
        update=j.split("*")[0]
        print(update)
        #all_sentences.append(update)
        file.write(update)

    file.close()


