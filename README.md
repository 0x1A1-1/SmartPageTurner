# Smart Page Turner
Hack Illinois hackathon project. Automate eye gaze tracker for assistive reading with OpenCV.


## Gaze Detection
Dependencies needed for the gaze detection:
- OpenCV
- dlib
- numpy
- imutils
- scipy
- shape_predictor_68_face_landmarks.dat 

#### To run the python module:
```
python landmark_with_center.py --shape-predictor shape_predictor_68_face_landmarks.dat --camera 0
```
*if you want to use external webcam, change camera param to 1


#### To change threshold for detection:
```
FRAME_THRESHOLD = 10
RATIO_THRESHOLD_LB = 0.45
RATIO_THRESHOLD_UB = 0.55
```


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
