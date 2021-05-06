from PIL import Image, ImageDraw
import face_recognition

image_of_trump = face_recognition.load_image_file('./img/groups/trump1.jpeg')
trump_face_encoding = face_recognition.face_encodings(image_of_trump)[0]

image_of_obama = face_recognition.load_image_file('./img/groups/obama1.jpeg')
obama_face_encoding = face_recognition.face_encodings(image_of_obama)[0]

# Create an array of encodings and names
known_face_encodings = [trump_face_encoding, obama_face_encoding]

known_face_names = ['Trump', 'Obama']

# Load test image
test_image = face_recognition.load_image_file('./img/groups/obama_trump1.jpeg')

# Find faces in test_image
face_locations = face_recognition.face_locations(test_image)

face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Conver to PIL format so we can write on it
pil_image = Image.fromarray(test_image)

# Create an ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through images in test image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = 'Unknown'
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

del draw

pil_image.show()