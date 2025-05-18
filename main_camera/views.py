import base64
import os
import cv2
import numpy as np
from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from tensorflow.keras.models import load_model

model = load_model("C:/Users/Lenovo/OneDrive/Desktop/diplom_ishi/faceproject/emotion_model_new.h5")
labels = ["g'azablangan", "jirkanish", "qo‘rqish", "xursand", "neytral", "xafa", "hayratlangan"]

def detect_emotion_view(request):
    if request.method == 'POST':
        image_data = request.POST.get('image')
        if image_data:
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            img_bytes = base64.b64decode(imgstr)

            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

            nparr = np.frombuffer(img_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) == 0:
                emotion = "Yuz aniqlanmadi"
                probability = ""
                # Yuz aniqlanmasa rasm saqlanmaydi yoki xohlasangiz saqlashingiz mumkin
                face_image_url = None
                image_url = None
            else:
                (x, y, w, h) = faces[0]
                face_img = gray[y:y+h, x:x+w]
                resized = cv2.resize(face_img, (48, 48))
                normalized = resized / 255.0
                reshaped = np.reshape(normalized, (1, 48, 48, 1))

                result = model.predict(reshaped)
                probabilities = result[0]
                label_index = np.argmax(probabilities)
                emotion = labels[label_index]
                probability = f"{probabilities[label_index]*100:.2f} %"

                base_folder = os.path.join(settings.MEDIA_ROOT, 'dataset', emotion)
                os.makedirs(base_folder, exist_ok=True)

                face_color = img[y:y+h, x:x+w]
                face_filename = f'{timestamp}_face.jpg'
                face_filepath = os.path.join(base_folder, face_filename)
                cv2.imwrite(face_filepath, face_color)

                face_image_url = settings.MEDIA_URL + f'dataset/{emotion}/{face_filename}'
                image_url = None

            return render(request, 'result.html', {
                'emotion': emotion,
                'probability': probability,
                'face_image_url': face_image_url,
                'image_url': image_url
            })

    return render(request, 'camera.html')
