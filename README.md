# Parkinson's Disease Detection System

## Overview
This project implements a machine learning system to detect Parkinson's disease from spiral drawings. The system uses Convolutional Neural Networks (CNNs) to analyze hand-drawn spirals and classify them as either from a healthy individual or someone with Parkinson's disease.

## Background
Parkinson's disease is a neurodegenerative disorder that affects movement control. One of the early symptoms is changes in handwriting and drawing abilities, known as micrographia. This project leverages this symptom by analyzing spiral drawings, which can reveal tremors and other motor impairments characteristic of Parkinson's disease.

## Project Structure
```
├── data/                  # Dataset storage
│   ├── spiral/            # Spiral drawing images
│   │   ├── training/      # Training dataset
│   │   └── testing/       # Testing dataset
│   └── wave/              # Wave drawing images (alternative dataset)
├── notebooks/             # Jupyter notebooks
│   ├── data_preprocessing.ipynb  # Data preparation
│   ├── model_training.ipynb      # Model development
│   └── model_evaluation.ipynb    # Performance assessment
├── src/                   # Source code
│   └── app.py             # Streamlit web application
├── models/                # Saved trained models
├── docs/                  # Project documentation
├── requirements.txt       # Dependencies
└── README.md              # Project overview
```

## Features
- **Data Preprocessing**: Techniques for image normalization and augmentation
- **CNN Model**: Deep learning architecture optimized for image classification
- **Performance Metrics**: Evaluation using accuracy, precision, and recall
- **Web Interface**: User-friendly Streamlit application for real-time predictions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Parkinsons-Detection.git
cd Parkinsons-Detection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application
```bash
cd src
streamlit run app.py
```

The application will open in your default web browser. Upload a spiral drawing image to get a prediction on whether it indicates Parkinson's disease or not.

### Training the Model
To retrain the model with your own data:

1. Place your spiral images in the appropriate directories under `data/spiral/`
2. Run the notebooks in sequence:
   - `data_preprocessing.ipynb`
   - `model_training.ipynb`
   - `model_evaluation.ipynb`

## Model Performance
The current model achieves:
- Accuracy: ~70%
- Precision: ~65%
- Recall: ~75%

## Future Improvements
- Implement data augmentation to improve model robustness
- Explore transfer learning with pre-trained models
- Add explainability features to highlight decision factors
- Incorporate wave drawings for multi-modal analysis

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Dataset providers
- TensorFlow and Keras teams
- Streamlit for the web application framework