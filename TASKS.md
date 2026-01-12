# Plant Disease Detector - Tasks

> **Project:** Plant Disease Detector  
> **Version:** 0.0.4  
> **Last Updated:** 2026-01-12

---

---

## ✅ Completed (v0.0.4)

### Machine Learning
- [x] Initial MobileNetV2 Transfer Learning pipeline.
- [x] Model export to H5 format.
- [x] Class label mapping generation.

### Backend
- [x] Django project setup and configuration.
- [x] Classifier app development.
- [x] Image upload processing with PIL.
- [x] PredictionResult database model.

### UI/UX
- [x] Bootstrap 5 responsive dashboard.
- [x] Plotly.js chart integration for confidence scores.
- [x] Scan history page with filtering.

---

## 🚧 In Progress

### Documentation
- [/] Refresh all documentation files to new templates.
  - README, CHANGELOG, DEVELOPMENT, LICENSE, TASKS.

---

## 📋 To Do

### High Priority
- [ ] **Expand Dataset**: Include more plant types (Tomato, Grape, etc.).
- [ ] **API Access**: Implement REST endpoints for mobile app support.

### Medium Priority
- [ ] **Dockerization**: Create a Dockerfile for easy deployment.
- [ ] **Inference Optimization**: Switch to TFLite for faster CPU inference.

### Low Priority
- [ ] **PWA Support**: Allow offline viewing of scan history.

---

## 🐛 Bug Fixes

- [ ] **BUG-1:** Large images (8MB+) cause timeout in development server.
  - Implement async processing or resizing on client-side.

---

## 💡 Ideas / Future

- Real-time video stream analysis.
- Integration with plant care advice based on detected disease.

---

## 🏗️ Architecture Notes

- Current inference is synchronous; consider Celery if expanding to many concurrent users.
- Model is loaded into memory on the first request; lazy-loading is efficient for low-traffic sites.

---
