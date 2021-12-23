# Facial-Login-System
This dlib-based facial login system is a technology capable of matching a human face from a digital webcam frame capture against a database[number of Numpy Arrays - 128 computer 128-d (i.e., a list of 128 real-valued numbers) that is used to quantify the face] of faces, typically employed to authenticate users through ID verification services, works by pinpointing and measuring facial features from a given image.

# INSTALLATION-
Before using the code, first make sure you have installed the appropriate Python Libraries! Or else, the code won't execute!

**LIST -**

#1. I'm assuming you are already familiar with the OpenCV Python library used in the Computer Vision Field.
(i.e., ```pip install opencv-contrib-python```) - Pre-built CPU-only OpenCV package.

#2. Install a .cpp[C++] based compiler so that the dlib python library will execute on Python platform!
(i.e., Install Visual Studio Community 2019 and in the Workloads, select "DESKTOP DEVELOPMENT WITH C++")

#3. Install DLib python library using pip command! Dlib is a general purpose cross-platform software library written in the programming language C++. You will have trouble installing these packages. Refer to online sources to install these python packages!
(i.e., ```pip install dlib```) - This command tries to download either (.whl - wheel file) or (.tar.gz - tar ball file) from https://pypi.org/project/dlib/#files

#4. Install CMake python library!
(i.e., ```pip install cmake```) - CMake is used to control the software compilation process using simple platform and compiler independent configuration files, and generate native makefiles and workspaces that can be used in the compiler environment of your choice.

#5. And finally, install Face Recognition Library that makes use of DLib and all the other previously mentioned libraries!
(i.e., ```pip install face-recognition```) - Recognize and manipulate faces from Python or from the command line with
the world’s simplest face recognition library.
Built using dlib’s state-of-the-art face recognition
built with deep learning. The model has an accuracy of 99.38% on the
Labeled Faces in the Wild benchmark.

#6. This next library is important only if you are using the code for "Facial-Login-Via-Internet" folder!
(i.e., ```pip install imagekitio```) - library for storing images online!
Make sure you register and get the keys arranged for yourself!

```
from imagekitio import ImageKit
imagekit = ImageKit(
    private_key='your private_key',
    public_key='your public_key',
    url_endpoint = 'your url_endpoint'
)
```

**NOTE: It's not necessary if you use the code for "Facial-Login-Via-No-Internet", because there it only uses numpy(.npy) files to store the 128-d array data of your face landmarks and uses them to authenticate!**

# HOW TO USE IT-

There's no explanation required on how to use the code as it's pretty self-explanatory and easy to use!
For instance, I have already registered with an account UsernameID - **3b890a3f** that belongs to **Elon Musk**.
You can login with his ID and see if it recognizes Elon Musk's face!
