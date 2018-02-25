# OpenCV-Triggered
Hack Illinois hack project. Automate eye gaze tracker for reading ( DUDE CHILL )


## Gaze Detection
Dependencies needed for the gaze detection:
- OpenCV
- dlib
- numpy
- imutils
- scipy

To run the python module:
```
python landmark_with_center.py --shape-predictor shape_predictor_68_face_landmarks.dat --camera 0
```
***if you want to use external webcam, change camera param to 1


## Web host
Web page for simple proof of concept of page turning.

To run the web host, first run  
```
ifconfig   (LINUX)
ipconfig   (WINDOWS)
```
to get your ip address and swap it within `index.html` file

Then run
```
npm install
node app.js
```
