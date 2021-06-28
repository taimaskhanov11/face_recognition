import face_recognition
from PIL import Image, ImageDraw


def face_rec():
    olsen_face_img = face_recognition.load_image_file('img/elizabeth-olsen-wallpaper-35798-6598739.jpeg')
    olsen_face_location = face_recognition.face_locations(olsen_face_img)

    avengers_img = face_recognition.load_image_file('img/5266843-andy-serkis-robert-downey-jr-aaron-taylor-johnson.jpg')
    avengers_img_faces_locations = face_recognition.face_locations(avengers_img)

    print(olsen_face_location)
    print(avengers_img_faces_locations)
    print(f'Found {len(olsen_face_location)} face(s) in this image')
    print(f'Found {len(avengers_img_faces_locations)} face(s) in this image')

    pil_img1 = Image.fromarray(olsen_face_img)
    draw1 = ImageDraw.Draw(pil_img1)
    for (top, right, bottom, left) in olsen_face_location:
        draw1.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

    del draw1
    pil_img1.save('img/new_olsen1.jpg')

    pil_img2 = Image.fromarray(avengers_img)
    draw2 = ImageDraw.Draw(pil_img2)
    for (top, right, bottom, left) in avengers_img_faces_locations:
        draw2.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=4)

    del draw2
    pil_img2.save('img/new_avengers.jpg')


def extracting_faces(img_path):
    count = 0
    faces = face_recognition.load_image_file(img_path)
    faces_locations = face_recognition.face_locations(faces)

    for faces_location in faces_locations:
        top, right, bottom, left = faces_location

        face_img = faces[top:bottom, left:right]
        pil_img = Image.fromarray(face_img)
        pil_img.save(f"img/{count}_face_img.jpg")
        count += 1

    return f'Found {count} faces(s) in this photo'


def compare_faces(img1_path, img2_path):
    img1 = face_recognition.load_image_file(img1_path)
    img1_encodings = face_recognition.face_encodings(img1)[0]
    # print(img1_encodings)

    img2 = face_recognition.load_image_file(img2_path)
    img2_encodings = face_recognition.face_encodings(img2)[0]

    result = face_recognition.compare_faces([img1_encodings], img2_encodings)
    # print(result)

    if result[0]:
        print("Welcome to the club! :*")
    else:
        print('Sorry not today...')


def main():
    # face_rec()
    # print(extracting_faces('img/avengers-age-of-ultron-7017.jpg'))
    # print(extracting_faces('img/5266843-andy-serkis-robert-downey-jr-aaron-taylor-johnson.jpg'))
    # compare_faces('img/elizabeth-olsen-wallpaper-35798-6598739.jpeg', 'img/olsen2.jpg')
    # compare_faces('img/elizabeth-olsen-wallpaper-35798-6598739.jpeg',
    #               'img/skarlett-yokhansson-v-epokhu-ultron-shpalery-2560x2048_33.jpg')
    compare_faces('img/elizabeth-olsen-wallpaper-35798-6598739.jpeg',
                  'img/Elizabeth-Olsen -Wind-River-Photocall--03.jpg')


if __name__ == '__main__':
    main()
