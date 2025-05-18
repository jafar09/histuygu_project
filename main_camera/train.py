import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint

# Parametrlar
img_width, img_height = 48, 48
batch_size = 32
epochs = 20
num_classes = 7  # FER-2013 da 7 ta emotsiya mavjud

# Data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=15,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)

# Train va Test generator
train_generator = train_datagen.flow_from_directory(
    "C:/Users/Lenovo/OneDrive/Desktop/diplom_ishi/faceproject/dataset/train",  # <- FER-2013 train papkasi yo'li
    target_size=(img_width, img_height),
    color_mode="grayscale",
    batch_size=batch_size,
    class_mode="categorical"
)

val_generator = ImageDataGenerator(rescale=1./255).flow_from_directory(
    "C:/Users/Lenovo/OneDrive/Desktop/diplom_ishi/faceproject/dataset/test",  # <- FER-2013 test papkasi yo'li
    target_size=(img_width, img_height),
    color_mode="grayscale",
    batch_size=batch_size,
    class_mode="categorical"
)

# Model yaratish
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 1)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

# Modelni compile qilish
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Eng yaxshi modelni saqlash
checkpoint = ModelCheckpoint("emotion_model_new.h5", monitor='val_accuracy', save_best_only=True, mode='max')

# Modelni o'qitish
model.fit(train_generator, validation_data=val_generator, epochs=epochs, callbacks=[checkpoint])
