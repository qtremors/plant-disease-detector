<p align="center">
  <img src="assets/plant-disease-detector-preview.jpg" alt="Plant Disease Detector Banner" width="350" style="border-radius: 20px;"/>
</p>

<h1 align="center"><a href="https://github.com/qtremors/plant-disease-detector">Plant Disease Detector</a></h1>

<p align="center">
  A robust Django-based web application utilizing TensorFlow and MobileNetV2 for the detection of apple leaf diseases.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-5.0-092E20?logo=django" alt="Django">
  <img src="https://img.shields.io/badge/TensorFlow-2.15-FF6F00?logo=tensorflow" alt="TensorFlow">
  <img src="https://img.shields.io/badge/uv-Package_Manager-4B5EAA?logo=python" alt="uv">
  <img src="https://img.shields.io/badge/License-TSL-red" alt="License">
</p>

> [!NOTE]
> **Personal Project** 🎯 I built this to demonstrate the end-to-end integration of deep learning models into a modern web framework, focusing on performance and user experience.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ⚡ **High-Performance Inference** | Powered by a MobileNetV2 model using Transfer Learning for fast and accurate results. |
| 📂 **Drag-and-Drop Interface** | Intuitive Bootstrap-based UI allowing users to easily upload images for analysis. |
| 📊 **Interactive Visualization** | Dynamic probability charts rendered with Plotly.js to show model confidence across all classes. |
| 💾 **History Tracking** | Automatically saves prediction results and images to a local SQLite database for future reference. |

---

## ⚠️ Important Disclaimers & Limitations

This is a **student/portfolio project** designed for educational purposes. Please be aware of the following technical limitations:

### 1. Limited Scope (Apple Leaves Only)
This model was trained on a specific subset of the **PlantVillage dataset** containing **only apple leaves**. It does **not** have an "Unknown" or "Background" class.
* **Result:** If you upload an image of a different plant (e.g., a tomato leaf) or a non-plant object (e.g., a cat, a car), the model will **incorrectly classify it** as one of the apple diseases with high confidence.
* **Why?** The model's final layer (Softmax) forces all predictions to sum to 100%, compelling it to choose the "closest match" even if the input is completely unrelated.

### 2. Production Readiness
This application is **not** intended for actual agricultural use. Real-world field conditions (bad lighting, blurry photos, multiple leaves in frame) may significantly affect accuracy.

---

## 📸 Screenshots

| Apple scab input | Apple scab output |
|:---------:|:------------:|
| ![Apple scab input](assets/apple-scab-input.png) | ![Apple scab output](assets/apple-scab-output.png) |

| Random input | History Page |
|:---------:|:------------:|
| ![Random input](assets/random.png) | ![History Page](assets/history.png) |

---

## ✅ Recognized Classes

The model is specifically trained to identify the following conditions on **Apple Leaves**:

| Class Label | Description |
| :--- | :--- |
| **Apple Scab** | Fungal disease causing dark, scabby spots on leaves. |
| **Black Rot** | Fungal disease causing circular brown spots and fruit rot. |
| **Cedar Apple Rust** | Fungal disease appearing as bright orange/yellow spots. |
| **Healthy** | A healthy apple leaf with no visible symptoms. |

---

## 📋 Prerequisites

Ensure you have the following installed on your system:

*   **Python 3.11+**
*   **uv**

---

## 🚀 Quick Start

```bash
# Clone and navigate
git clone https://github.com/qtremors/plant-disease-detector.git
cd plant-disease-detector

# Install dependencies
uv sync

# Setup environment
cp .env.example .env

# Initialize Database
uv run python manage.py migrate

# Run the project
uv run python manage.py runserver
```

Visit **http://127.0.0.1:8000/**

---

## 🕹 Usage Guide

1.  **Open the App:** Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.
2.  **Upload:** Drag and drop an image of an apple leaf into the upload area or click to select a file.
3.  **Analyze:** Click the **"Analyze Leaf"** button.
4.  **View Results:**
    *   The **Prediction** card shows the most likely disease.
    *   The **Confidence Chart** visualizes the probability distribution.
5.  **Check History:** Click "View Scan History" in the navbar to see past uploads and their results.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Django 5.0, Python 3.11+ |
| **ML Engine** | TensorFlow 2.x / Keras (MobileNetV2) |
| **Frontend** | Bootstrap 5, Plotly.js |
| **Database** | SQLite3 |
| **Tooling** | uv (Package Manager) |

---

## 📁 Project Structure

```
plant-disease-detector/
├── classifier/           # Main Django App (Inference logic & UI)
│   ├── services.py       # AI Inference service layer
│   ├── models.py         # Database models for scan history
│   └── templates/        # UI templates
├── ml_models/            # Stored model artifacts (.h5, .json)
├── core/                 # Project configuration
├── DEVELOPMENT.md        # Developer documentation
├── CHANGELOG.md          # Version history
├── LICENSE.md            # License terms
└── README.md
```

---

## 📊 System Resource usage and impact

cpu: ~15% during inference
ram: ~450MB (Model in memory)
disk: ~30MB for model artifacts

---

## 🧪 Testing

```bash
# Run unit tests (standard Django test suite)
uv run python manage.py test
```

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [DEVELOPMENT.md](DEVELOPMENT.md) | Architecture, setup, ML training details |
| [CHANGELOG.md](CHANGELOG.md) | Version history and release notes |
| [LICENSE.md](LICENSE.md) | License terms and attribution |

---

## 📄 License

**Tremors Source License (TSL)** - Source-available license allowing viewing, forking, and derivative works with **mandatory attribution**. Commercial use requires written permission.

See [LICENSE.md](LICENSE.md) for full terms.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/qtremors">Tremors</a>
</p>
