# DermaVision AI — New Professional Prototype

A fresh Flask prototype for the college project **Skin Cancer Classification Using Deep Learning**.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`.

## Included
- Premium medical-AI dashboard
- Image upload / drag & drop
- Model selector: Custom CNN, ResNet50, EfficientNetB0
- 7-class project context
- Prediction and confidence UI
- Class-probability bars
- Grad-CAM visualization layer
- Responsive layout
- Supplied sample lesion image for instant demo

## Important
The browser prediction values are **simulated demonstration values**. They are not real clinical predictions. Replace the demo JavaScript with the project's trained TensorFlow/Keras inference endpoint and actual Grad-CAM output when the trained model is available.
