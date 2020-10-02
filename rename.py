import os
import cv2


directory = r"D:\GitHub\gesture-based-rock-paper-scissor\image_data\nothing"
curr_num = 1

for entry in os.scandir(directory):
    im = cv2.imread(entry.path)
    new_name = str(curr_num)+".jpg"
    curr_num+=1
    cv2.imwrite(new_name,im)
    print(curr_num-1)

print("done")