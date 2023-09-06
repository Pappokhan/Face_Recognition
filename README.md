# Face_Recognition
Face recognition using the OpenCV and face_recognition libraries. It captures video from your computer's camera, detects faces in the video frames, and tries to recognize them by comparing them to a list of known faces. 
---
<p align="center"><img src="https://viterbischool.usc.edu/wp-content/uploads/2022/12/USC-ISI-1200x600-29.png"></p>


<h1>Face Recognition Code Explanation</h1>
    <h2>Imports:</h2>
    <p>Import the necessary libraries, including OpenCV (CV2) and face_recognition, for face detection and recognition.</p>

  <h2>Load Haar Cascade Classifier:</h2>
    <p>Load the Haar Cascade Classifier for detecting frontal faces from the OpenCV data.</p>

  <h2>Initialize Lists for Known Faces:</h2>
    <p>Create empty lists (known_faces and known_names) to store the known faces' encodings and corresponding names.</p>

  <h2>Load Known Faces and Encodings:</h2>
    <p>Load images of known individuals (Sundar Pichai, Jeff Bezos, Tim Cook, Elon Musk, and Bill Gates) using
        face_recognition.load_image_file and calculate their face encodings. Append these encodings and corresponding
        names to the respective lists.</p>

  <h2>Open a Video Capture:</h2>
    <p>Initialize a video capture object (cap) to access the webcam or camera feed (you specified index 0).</p>

  <h2>Real-time Face Recognition Loop:</h2>
    <p>Enter a continuous loop for real-time face recognition.</p>

  <h2>Read Frame from Webcam:</h2>
    <p>Capture a frame from the video feed using cap.read().</p>

  <h2>Face Detection:</h2>
    <p>Convert the frame to grayscale (gray) and use the Haar Cascade Classifier to detect faces
        (face_cascade.detectMultiScale). These detected faces are drawn as rectangles on the frame.</p>

  <h2>Face Recognition:</h2>
    <p>Convert the frame to RGB format (rgb_frame) since the face_recognition library requires RGB images. 
      Use
        face_recognition.face_locations to find face locations in the frame. For each detected face, extract the face
        image, calculate its encoding, and compare it to the known faces' encodings. If a match is found, assign the
        corresponding name; otherwise, it remains "Unknown."</p>

  <h2>Display Recognition Results:</h2>
    <p>Draw rectangles around detected faces and display the recognized names or "unknown" on the frame using OpenCV
        functions (cv2.rectangle and cv2.putText).</p>

  <h2>Exit the Loop:</h2>
    <p>The loop continues until you press the 'q' key, at which point it releases the video capture object and closes
        all OpenCV windows.</p>

  <h2>Clean Up:</h2>
    <p>Release the video capture and destroy all OpenCV windows.</p>
