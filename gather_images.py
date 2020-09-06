import cv2
import os
import sys

try:
    file_read = open("last_count.txt",'r')
except:
    file = open("last_count.txt",'w')
    file.write("rock 1 paper 1 scissor 1")
    file.close()
    file_read = open("last_count.txt",'r')

try:
    label_name = sys.argv[1]
    num_samples = int(sys.argv[2])
except:
    print("Image Class Argument missing !")
    exit(-1)

IMG_SAVE_PATH = 'image_data'
IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, label_name)

try:
    os.mkdir(IMG_SAVE_PATH)
except FileExistsError:
    pass
try:
    os.mkdir(IMG_CLASS_PATH)
except FileExistsError:
    print("{} directory already exists.".format(IMG_CLASS_PATH))

cap = cv2.VideoCapture(0)

start = False

#determining file numbering convention
x = file_read.read()
x = list(map(str,x.split()))
print(x)
if label_name=="rock":
    count = int(x[1])
elif label_name=="paper":
    count = int(x[3])
else:
    count = int(x[5])

#name convention correction for loop termination        
num_samples+=(count-1)

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    
    

    if count == num_samples:
        break

    cv2.rectangle(frame, (40, 60), (300, 300), (255, 255, 255), 2)

    if start:
        roi = frame[60:300, 60:300]
        save_path = os.path.join(IMG_CLASS_PATH, '{}.jpg'.format(count + 1))
        cv2.imwrite(save_path, roi)
        count += 1

    
    cv2.imshow("Collecting images for class "+str(sys.argv[1]), frame)

    k = cv2.waitKey(10)
    if k == ord('a'):
        start = not start

    if k == ord('q'):
        break

#writing file numbering for next time
file_read.close()
file_write = open("last_count.txt","w")
str_to_be_written = ""

if label_name=="rock":
    x[1] = str(count+1)
elif label_name=="paper":
    x[3] = str(count+1)
else:
    x[5] = str(count+1)


file_write.write(" ".join(x))
file_write.close()

print("\n{} image(s) saved to {}".format(count, IMG_CLASS_PATH))
cap.release()
cv2.destroyAllWindows()
