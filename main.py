import cv2
import face_recognition

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

known_faces = []
known_names = []

known_face_image_1 = face_recognition.load_image_file('Sundar pichai.jpg')
known_face_encoding_1 = face_recognition.face_encodings(known_face_image_1)[0]
known_faces.append(known_face_encoding_1)
known_names.append("Sundar Pichai")

known_face_image_2 = face_recognition.load_image_file('Jeff Bezos.jpg')
known_face_encoding_2 = face_recognition.face_encodings(known_face_image_2)[0]
known_faces.append(known_face_encoding_2)
known_names.append("Jeff Bezos")

known_face_image_3 = face_recognition.load_image_file('Tim Cook.jpg')
known_face_encoding_3 = face_recognition.face_encodings(known_face_image_3)[0]
known_faces.append(known_face_encoding_3)
known_names.append("Tim Cook")

known_face_image_4 = face_recognition.load_image_file('Elon musk.jpg')
known_face_encoding_4 = face_recognition.face_encodings(known_face_image_4)[0]
known_faces.append(known_face_encoding_4)
known_names.append("Elon Musk")

known_face_image_5 = face_recognition.load_image_file('Bill_Gates.jpg')
known_face_encoding_5 = face_recognition.face_encodings(known_face_image_5)[0]
known_faces.append(known_face_encoding_5)
known_names.append("Bill Gates")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face_image = rgb_frame[y:y + h, x:x + w]
        face_encodings = face_recognition.face_encodings(face_image)

        if len(face_encodings) > 0:
            matches = face_recognition.compare_faces(known_faces, face_encodings[0])
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_names[first_match_index]
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
