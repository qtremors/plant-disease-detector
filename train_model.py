import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
import os
import json

# --- Configuration ---
DATASET_PATH = r"Z:\datasets\Plant Diseases Dataset\New Plant Diseases Dataset(Augmented)"
TRAIN_DIR = os.path.join(DATASET_PATH, 'train')
VALID_DIR = os.path.join(DATASET_PATH, 'valid')

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

print(f"Checking dataset at: {DATASET_PATH}")
print(f"Training directory: {TRAIN_DIR}")

# --- Data Preparation ---
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

# Load Training Data
print("Loading training data...")
train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# Load Validation Data
print("Loading validation data...")
validation_generator = valid_datagen.flow_from_directory(
    VALID_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# --- Model Building (MobileNetV2) ---
print("Building model...")
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False  # Freeze base layers

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
# Automatically detect number of classes (should be 4 for Apple)
predictions = Dense(train_generator.num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# --- Training ---
print("Starting training (5 epochs)...")
history = model.fit(
    train_generator,
    epochs=5,
    validation_data=validation_generator
)

# --- Save Artifacts ---
print("Saving model and labels...")
model.save('plant_disease_model.h5')

# Save the class mapping (e.g., 0 -> Apple Scab)
class_indices = train_generator.class_indices
labels = {v: k for k, v in class_indices.items()}

with open('class_labels.json', 'w') as f:
    json.dump(labels, f)

print("✅ SUCCESS: 'plant_disease_model.h5' and 'class_labels.json' created!")