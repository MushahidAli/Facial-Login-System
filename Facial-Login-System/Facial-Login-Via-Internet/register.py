import os
import cv2
import face_recognition
from imagekitio import ImageKit

cap = cv2.VideoCapture(0)
while True:
    return_value,image = cap.read()
    cv2.imshow('INPUT - Press S To ScreenShot!',image)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('id.jpg',image)
        break
cap.release()
cv2.destroyAllWindows()

errorchecking = face_recognition.load_image_file("id.jpg")
try:
  error_code = face_recognition.face_encodings(errorchecking)[0]
except:
  os.system("cls")
  print("Facial Error!\nPlease Use Your Full Face Image Correctly!")
  os.remove("id.jpg");
  exit()

imagekit = ImageKit(
    private_key='private_=U/oOY9GSaaaTff4k2W4o5t53fUq',
    public_key='public_=0CO8Za9flCPeGRxutlgQvLYvkea',
    url_endpoint='https://ik.imagekit.io/zhfxaap2nx3'
)
upload = imagekit.upload(
    file=open("id.jpg", "rb"),
    file_name="id.jpg",
)
number = imagekit.list_files({
})


os.remove("id.jpg");
name = str(upload['response']['name'])
check = len(name)-4
os.system("cls")
print("Welcome To Mushahid Ali Solutions!\nThere Are Currently "+str(len(number['response']))+" Users Registered Including You!\nCONGRATULATIONS!")
print("\nYour Registered UsernameID Is : "+name[0:check])