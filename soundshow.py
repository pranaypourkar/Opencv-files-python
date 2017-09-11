# Author: Pranay 
import cv2
import numpy as np
import pyaudio
import wave


#img = cv2.imread('/home/pranay/Desktop/task1_lm_set2 (1)/set-2/2. Task_Description/test_images/board_2.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('/home/pranay/Desktop/task1_lm_set2 (1)/set-2/2. Task_Description/test_images/board_2.jpg')
cv2.imshow('image',img)


chunk = 1024
wf = wave.open('/home/pranay/Music/wav/bird.wav', 'rb')
p = pyaudio.PyAudio()

stream = p.open(
    format = p.get_format_from_width(wf.getsampwidth()),
    channels = wf.getnchannels(),
    rate = wf.getframerate(),
    output = True)
data = wf.readframes(chunk)

while data != '':
    stream.write(data)
    data = wf.readframes(chunk)

stream.close()
p.terminate()

cv2.waitKey(0)
cv2.destroyAllWindows()
