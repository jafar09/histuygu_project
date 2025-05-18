import os
import cv2
import numpy as np
from datetime import datetime
from tensorflow.keras.models import load_model

# Modelni yuklash
model = load_model("C:/Users/Lenovo/OneDrive/Desktop/diplom_ishi/faceproject/emotion_model_new.h5")

# 7 ta emotsiya (Uzbekchaga tarjimasi bilan)
labels = ["g'azablangan", "jirkanish", "qo‘rqish", "xursand", "neytral", "xafa", "hayratlangan"]

# Papkalarni yaratish (agar mavjud bo'lmasa)
for label in labels:
    os.makedirs(f"dataset/{label}", exist_ok=True)

# Yuzni aniqlovchi model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Kamera ishga tushadi
cap = cv2.VideoCapture(0)

print("Boshlanmoqda... 's' - saqlash, 'q' - chiqish")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera ochilmadi.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    detected_label = None
    face_img_to_save = None

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        gray_face = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray_face, (48, 48))
        normalized = resized / 255.0
        reshaped = np.reshape(normalized, (1, 48, 48, 1))

        result = model.predict(reshaped)
        probabilities = result[0]
        print(f"Ehtimollar: {probabilities}")

        label_index = np.argmax(probabilities)
        detected_label = labels[label_index]

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.putText(frame, f"{detected_label}: {probabilities[label_index]:.2f}", 
                    (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        face_img_to_save = face_img

    cv2.imshow("Emotion Detector", frame)

    key = cv2.waitKey(1)

    if key & 0xFF == ord('s') and detected_label and face_img_to_save is not None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"dataset/{detected_label}/{timestamp}.jpg"
        cv2.imwrite(filename, face_img_to_save)
        print(f"[+] Rasm saqlandi: {filename}")

    elif key & 0xFF == ord('q'):
        print("Dastur to'xtatildi.")
        break

cap.release()
cv2.destroyAllWindows()
