import os
import cv2
import numpy as np
import face_recognition

cap = cv2.VideoCapture(0)
while True:
    return_value,image = cap.read()
    cv2.imshow('INPUT - Press S To ScreenShot!',image)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('screenshotimage.jpg',image)
        break

cap.release()
cv2.destroyAllWindows()

os.system("cls")
img = face_recognition.load_image_file("screenshotimage.jpg")
try:
  valueOne = face_recognition.face_encodings(img)[0]
except:
  print("Facial Error!\nPlease Use Your Full Face Image Correctly!")
  os.remove("screenshotimage.jpg")
  exit()
os.system("cls")
os.remove("screenshotimage.jpg")

for filename in os.listdir("array_data/"):
    if filename.endswith(".npy"): 
         valueTwo = np.load("array_data/"+filename)
         result = face_recognition.compare_faces([valueOne], valueTwo)
         os.system("cls")
         if str(result) == "[True]":
            print("Welcome User - "+filename[0:len(filename)-4])
            break
         else:
              print("NULL EXISTENCE!")