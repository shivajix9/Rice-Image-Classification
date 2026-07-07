# 🌾 Rice Image Classification using CNN & Transfer Learning

## 📌 Project Overview

This project is a Deep Learning based image classification system that identifies different rice grain varieties from images.

The project uses a custom Convolutional Neural Network (CNN) and Transfer Learning techniques to classify rice images accurately.

The model predicts one of five rice categories:

- Arborio
- Basmati
- Ipsala
- Jasmine
- Karacadag

---

## 📂 Dataset

**Dataset:** Rice Image Dataset

Dataset contains:

- Total Images: 75,000
- Number of Classes: 5
- Images per Class: 15,000

The dataset is balanced and suitable for multi-class image classification.

---

# Phase 1: Data Understanding & CNN Modeling

## 🔍 Dataset Analysis

Performed:

- Number of class analysis
- Images per class count
- Image dimension checking
- Class distribution analysis
- Sample image visualization

---

## 🖼️ Data Preprocessing

Techniques applied:

- Image resizing (224×224)
- Normalization
- Train-validation split

---

## 🔄 Data Augmentation

Applied:

- Random Rotation
- Horizontal Flip
- Zoom
- Image Shift
- Contrast Adjustment

Augmentation improves model generalization and reduces overfitting.

---

## 🧠 Custom CNN Architecture

Built CNN model from scratch:

Architecture:

---
Input Image
↓
Convolution + ReLU
↓
Max Pooling
↓
Convolution + ReLU
↓
Max Pooling
↓
Convolution + ReLU
↓
Max Pooling
↓
Flatten
↓
Dense Layer
↓
Dropout
↓
Softmax Classifier

## 📊 Evaluation Metrics

Model evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Training progress monitored using:

- Accuracy Curve
- Loss Curve

---

## 🧪 CNN Experimentation

Different CNN architectures were tested by modifying:

- Number of convolution layers
- Filters
- Dropout
- Batch Normalization

Models were compared based on performance and overfitting behavior.

---

# Phase 2: Transfer Learning

Implemented pretrained deep learning models:

- MobileNetV2
- EfficientNet
- ResNet

---

## Transfer Learning Techniques

### Feature Extraction

- Loaded pretrained ImageNet models
- Frozen base layers
- Trained custom classifier head

### Fine Tuning

- Unfrozen selected layers
- Used lower learning rate
- Improved model performance

---

## Model Comparison

Compared:

- Custom CNN
- MobileNetV2
- EfficientNet
- ResNet

Based on:

- Accuracy
- Training Time
- Number of Parameters
- Model Size

---

# Deployment

A Streamlit web application was created.

Features:

- Upload rice image
- Image preprocessing
- Model prediction
- Display predicted rice variety

---

# Project Structure
Rice-Image-Classification/
│── app.py
│── rice_model.keras
│── requirements.txt
│── README.md
│── notebooks/
│── Phase1_CNN.ipynb
│── Phase2_TransferLearning.ipynb


---

# Technologies Used

- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

Results
The model successfully classifies rice grain images into five categories with high accuracy using CNN and Transfer Learning.
