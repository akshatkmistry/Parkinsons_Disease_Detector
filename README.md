# 🧠 Parkinson's Disease Detector

<div align="center">
  <img src="[![image](https://github.com/user-attachments/assets/3e59f8a7-1105-448c-b2f2-0e721f839925)](https://mir-s3-cdn-cf.behance.net/project_modules/disp/48341e34539809.56d4b610ee304.gif)" width="300" alt="Spiral Drawing">
</div>

A deep learning-based web app that detects **Parkinson's Disease** from **spiral drawings** using a Convolutional Neural Network (CNN) built with TensorFlow/Keras and deployed via **Streamlit**.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://parkinsons-disease-detector.streamlit.app)  

---

## 🚀 Features

- 🧪 **Model**: Trained CNN to classify spiral drawings as `healthy` or `parkinson` with **73.33% accuracy**.
- 📤 **Web App**: Upload a 128×128 pixel spiral image to get real-time predictions.
- 📊 **Visualizations**: Training/validation accuracy plots and sample predictions included.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/akshatkmistry/Parkinsons_Disease_Detector.git
cd Parkinsons_Disease_Detector
```

### 2. Set Up Environment

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Locally

```bash
streamlit run src/app.py
```

---

## 🧾 Dependencies

**Python**: 3.12

### Python Packages (`requirements.txt`)
```plaintext
 numpy
opencv-python-headless
tensorflow
scikit-learn
matplotlib
seaborn
streamlit
```

### System Packages (`packages.txt`)
Required for **Streamlit Cloud** deployment:

```plaintext
libsm6  
libxext6  
libxrender-dev  
libglib2.0-0  
```

---

## 🧠 Usage

- **Web App**: Upload a spiral image (`128x128`, PNG or JPG). The app returns whether the drawing is from a person with Parkinson’s or not.

---

## 📈 Results

| Metric     | Value   |
|------------|---------|
| Accuracy   | 73.33%  |
| Precision  | 0.89    |
| Recall     | 0.53    |
| F1-Score   | 0.67    |

---

## 🤝 Contributing

Contributions are welcome!  
Follow these steps:

1. Fork the repository  
2. Create a new branch: `git checkout -b feature-branch`  
3. Commit your changes: `git commit -m "Add feature"`  
4. Push to your branch: `git push origin feature-branch`  
5. Open a Pull Request

---

## 📄 License

**MIT License**  
© Akshat Mistry, 2025

