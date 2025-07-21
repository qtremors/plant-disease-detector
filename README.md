# 🌿 Plant Disease Detector

A web application built with **Django** and **TensorFlow** that detects **apple leaf diseases** using deep learning. Upload an image of a leaf, and the app will predict the plant’s health status with confidence scores.

> 📸 *Insert a screenshot of your application here*

---

## ⚠️ Model Limitations

🚧 This is a **proof-of-concept** model trained **only on apple leaf images**.

### ✅ Recognized Classes:

* Apple Scab 🍏
* Apple Black Rot 🍎
* Apple Cedar Rust 🌲
* Healthy Apple Leaf ✅

❗ **Important:** If you upload leaves from other plants (e.g., corn, tomato, potato), the model will still attempt to classify them as one of the above apple categories. It is not trained for other species.

---

## ✨ Features

* 📄 Upload leaf images via a simple web UI
* 🤖 Deep learning predictions using **MobileNetV2**
* 📊 Interactive **Plotly** bar chart for top-3 predictions
* 📱 Fully responsive layout using **Bootstrap 5**

---

## 🛠️ Tech Stack

| Layer         | Technology Used                 |
| ------------- | ------------------------------- |
| Backend       | Django                          |
| Frontend      | HTML, Bootstrap 5               |
| ML Model      | TensorFlow, Keras (MobileNetV2) |
| Visualization | Plotly                          |
| Libraries     | Pillow, NumPy                   |

---

## 🚀 Getting Started

### 1. Prerequisites

* Python 3.8+
* Git

### 2. Clone the Repository

```bash
git clone <your-repository-url>
cd plant-disease-detector
```

### 3. Create Virtual Environment

**Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Model Training (Optional)

### 5. Download Dataset

* Download the **New Plant Diseases Dataset (Augmented)** from [Kaggle](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
* Unzip into the project root folder

### 6. Filter for Apple Leaf Data Only

In both `train/` and `valid/` folders, **keep only**:

```
Apple___Apple_scab
Apple___Black_rot
Apple___Cedar_apple_rust
Apple___healthy
```

### 7. Train the Model

```bash
python train_model.py
```

This will generate:

* `plant_disease_model.h5`
* `class_labels.json`

---

## 🌐 Run the Application

```bash
python manage.py migrate
python manage.py runserver
```

Open your browser and visit:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📈 Future Improvements

* 🔍 Retrain model with the full **PlantVillage** dataset to support multiple plant types and diseases
* 🗌️ Add location tracking using **Leaflet.js** and the **Geolocation API**
* 🎯 Improve accuracy through model tuning and experimentation
* ☁️ Deploy to **Heroku**, **AWS**, or **GCP** for public use

---

## 📄 License

[MIT](LICENSE)

---

## 🙌 Acknowledgements

* [PlantVillage Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
* [TensorFlow](https://www.tensorflow.org/)
* [Django](https://www.djangoproject.com/)
