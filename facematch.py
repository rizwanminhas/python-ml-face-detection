import face_recognition

image_of_trump = face_recognition.load_image_file('./img/groups/trump1.jpeg')
trump_face_encoding = face_recognition.face_encodings(image_of_trump)[0]

unknown_image = face_recognition.load_image_file('./img/groups/trump2.jpeg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([trump_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Trump')
else:
    print('This is NOT Trump')

