
import time
import pandas as pd
import cv2
import pytesseract

frame_count = 0
fps = 0
timestamps = 0
flag_is_sentence_exists=0
flag_first_sentence=0
startTime=0.0
path=""
parsed_data={}
firstData=""
parsed_data_to_push={}

def parse_video(time, data):

    dataToPush = []
    global flag_is_sentence_exists
    global flag_first_sentence
    global firstData
    global fps
    if flag_is_sentence_exists == 0:
        parsed_data[0] = data
        firstData = data
        flag_is_sentence_exists = 1
    global startTime
    global frame_count
    frame_count += 1
    timestamps = (float(frame_count) / fps) + 1
    if data != '' and time not in parsed_data.keys():
        if data not in parsed_data.values():
            if flag_first_sentence == 0:
                dataToPush.append(firstData)
                dataToPush.append(0.0)
                dataToPush.append(timestamps)
                parsed_data_to_push[0] = dataToPush
                flag_first_sentence = 1
            else:
                dataToPush.append(data)
                dataToPush.append(startTime)
                dataToPush.append(timestamps)
                parsed_data_to_push[time] = dataToPush
                parsed_data[time] = data
                duration = ((timestamps - startTime))

            startTime = timestamps


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


def parse(data):
    '''Function to parse data from detected text'''
    not_nes = ['\\', '/', '!', '~', '`', '|', '-', '=']
    parsed = []
    last_word = ''
    for word in data:
        if word != '' and word not in not_nes:
            parsed.append(word)
            last_word = word

    return " ".join(parsed)


def OCRFunction(video_path):
    global path
    path= video_path
    video = cv2.VideoCapture(path)
    global fps
    fps = video.get(cv2.CAP_PROP_FPS)
    global timestamps
    timestamps = [video.get(cv2.CAP_PROP_POS_MSEC)]
    custom_config = r'--oem 1 --psm 6'
    start = time.time()
    while True:
        ret, frame = video.read()
        now = round(time.time() - start)
        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Converting to GRAY scale as
            binary_frame = cv2.threshold(gray_frame, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[
                1]  # Performing simple thresholding with OTSU binarization
            frame_info = pytesseract.image_to_data(binary_frame, output_type=pytesseract.Output.DICT, config=custom_config,
                                                   lang='eng')
            fm = frame.copy()
            total_boxes = len(frame_info['text'])  # length of total no of blocks detected
            for sequence_number in range(total_boxes):  # Looping through blocks
                if float(frame_info['conf'][
                           sequence_number]) > 30:  # if confidence of box being text if greater than 30 (30-40 is optimal limit)
                    (x, y, w, h) = (frame_info['left'][sequence_number], frame_info['top'][sequence_number],
                                    frame_info['width'][sequence_number],
                                    frame_info['height'][sequence_number])  # get the coordinates of confident blocks
                    fm = cv2.rectangle(fm, (x, y), (x + w, y + h), (0, 255, 0),
                                       1)  # Drawing a rectangle box over confident word
            parsed = parse(frame_info['text'])

            parse_video(now, parsed)
            if cv2.waitKey(1) == 27:
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()
    df=pd.DataFrame(parsed_data_to_push,index=['data','startTime','endTime']).T
    path_of_csv=r"C:\Users\324868629\Desktop\project updated\Codalleh-AnyClip\OCR\video_data.csv"
    df.to_csv(path_of_csv)
    return path_of_csv
