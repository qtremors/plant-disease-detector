# Plant Disease Detector - Developer Documentation

> Comprehensive documentation for developers working on the Plant Disease Detector.

**Version:** 1.0.0 | **Last Updated:** 2026-01-12

---

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [API Routes](#api-routes)
- [Environment Variables](#environment-variables)
- [ML Pipeline](#ml-pipeline)
- [Testing](#testing)

---

## Architecture Overview

Plant Disease Detector follows a **Service-Based Django** architecture:

```
┌──────────────────────────────────────────────────────────────┐
│                        Frontend Layer                        │
│             Bootstrap 5 + Plotly.js + Vanilla JS             │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                        Backend Layer                         │
│             Django 5.0 (Views, Forms, ORM)                   │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                        Service Layer                         │
│            TensorFlow/Keras Inference Engine                 │
└──────────────────────────────────────────────────────────────┘
```

### Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **MobileNetV2** | Lightweight and efficient for real-time web inference. |
| **uv** | Provides lightning-fast dependency resolution and reproducible environments. |
| **Singleton Model Loader** | Ensures the multi-gigabyte model is loaded into memory only once. |

---

## Project Structure

```
plant-disease-detector/
├── classifier/               # Main Application logic
│   ├── services.py           # ML Model interface
│   ├── utils.py              # Chart generation logic
│   ├── views.py              # Web controllers
│   ├── models.py             # Database schema
│   └── templates/            # HTML Views
├── core/                     # Project settings and configuration
├── ml_models/                # Model weights (.h5) and class labels
├── media/                    # User uploaded scans
├── train_model.py            # Model training script
├── pyproject.toml            # Project dependencies
└── uv.lock                   # Dependency lock file
```

---

## Database Schema

### Models Overview (1 total)

| Model | Purpose | Key Fields |
|-------|---------|------------|
| **PredictionResult** | Stores scan history | `image`, `predicted_label`, `confidence`, `created_at` |

---

## API Routes

### Base Routes

| Method | Path | Handler | Description |
|--------|------|---------|-------------|
| GET/POST | `/` | `views.index` | Main upload and analysis interface |
| GET | `/history/` | `views.history` | View list of past scans |

---

## Environment Variables

### Required

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django security key | `your-secret-key-here` |
| `DEBUG` | Enable/Disable debug mode | `True` |

---

## ML Pipeline

### Training
The model is trained using `train_model.py` which leverages **Transfer Learning** with the following architecture:

1.  **Base:** MobileNetV2 (frozen weights, pre-trained on ImageNet).
2.  **Head:** GlobalAveragePooling2D → Dense (1024, ReLU) → Output Dense (4, Softmax).
3.  **Dataset:** [New Plant Diseases Dataset (Augmented)](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) sourced via `kagglehub`.
4.  **Training:** Trained for 5 epochs using the Adam optimizer (`lr=0.001`).

#### Detailed Retraining Steps (Optional)

1.  **Dataset Preparation**: Use `kagglehub` to download the dataset. You can customize the download location by setting the `KAGGLEHUB_CACHE` environment variable:
    ```python
    import os
    # Set your custom directory (optional)
    os.environ["KAGGLEHUB_CACHE"] = r"Z:\datasets"

    import kagglehub
    # Download latest version
    path = kagglehub.dataset_download("vipoooool/new-plant-diseases-dataset")
    print("Path to dataset files:", path)
    ```
2.  **Configuration**: Open `train_model.py` and set `DATASET_PATH` to the path printed above.
    > [!NOTE]
    > Ensure you point to the augmented dataset folder within the download path (e.g., `.../New Plant Diseases Dataset(Augmented)`).
3.  **Execution**: Run the training script:
    ```bash
    uv run python train_model.py
    ```
4.  **Integration**: The script generates `ml_models/plant_disease_model.h5` and `ml_models/class_labels.json`, which the server loads on the next request.

### Inference
Managed in `classifier/services.py`:
- **Image Preprocessing**: Resized to 224x224, normalized to [0,1].
- **Prediction**: Returns top 3 most likely classes.
- **Loading Pattern**: Implements a **Singleton Model Loader** that ensures the multi-gigabyte model is loaded into memory only once, significantly reducing cold-start latency for subsequent requests.

---

## Testing

### Running Tests

```bash
# General Django tests
uv run python manage.py test
```

---

<p align="center">
  <a href="README.md">← Back to README</a>
</p>
