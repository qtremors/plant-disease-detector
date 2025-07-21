# train_model.py
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
import numpy as np
import json

# --- Configuration ---
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
DATASET_PATH = 'New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)' # Adjust this path

# --- Data Preparation ---
# Create data generators with augmentation for training and validation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

valid_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    f'{DATASET_PATH}/train',
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

validation_generator = valid_datagen.flow_from_directory(
    f'{DATASET_PATH}/valid',
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# --- Model Building (Transfer Learning) ---
# Load the base model (MobileNetV2) without the top classification layer
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the base model layers
base_model.trainable = False

# Add custom layers on top
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(train_generator.num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# --- Compile and Train the Model ---
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(
    train_generator,
    epochs=5, # Use more epochs for better accuracy (e.g., 10-20)
    validation_data=validation_generator
)

# --- Save the Model and Class Labels ---
print("Saving model...")
model.save('plant_disease_model.h5')

class_indices = train_generator.class_indices
# Invert the dictionary to map index to label
labels = {v: k for k, v in class_indices.items()}

with open('class_labels.json', 'w') as f:
    json.dump(labels, f)

print("Model and class labels saved successfully!")