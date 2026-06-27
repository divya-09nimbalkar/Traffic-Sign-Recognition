
---

```markdown
# 🚦 Traffic Sign Recognition

A computer vision project for classifying traffic signs using **PyTorch** and **ResNet18**.  
This repository demonstrates an end‑to‑end ML workflow: dataset preparation, model training, evaluation, testing, and interactive exploration via Jupyter notebooks.

---

## 📂 Project Structure
```
Traffic_Sign_Recognition/
│
├── data/
│   ├── raw/               # Raw traffic sign images
│   └── processed/         # Preprocessed dataset (class folders or CSV)
│
├── docs/                  # Documentation
│
├── models/
│   └── traffic_sign_resnet18.pth  # Saved model weights
│
├── notebooks/
│   └── exploration.ipynb  # Interactive notebook for inference
│
├── src/
│   ├── __init__.py
│   ├── data_pipeline.py   # Dataset + DataLoader
│   ├── model.py           # ResNet18 customization
│   ├── train.py           # Training loop
│   ├── evaluate.py        # Model loading + evaluation
│   ├── utils.py           # Helper functions
│   └── main.py            # Entry point
│
├── tests/
│   ├── test_data_pipeline.py
│   ├── test_model.py
│   └── test_utils.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/divya-09nimbalkar/Traffic_Sign_Recognition.git
   cd Traffic_Sign_Recognition
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate # Linux/Mac
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### Train & Evaluate
Run the pipeline:
```bash
python -m src.main
```

This will:
- Prepare data
- Build the ResNet18 model
- Train for 2 epochs
- Save weights to `models/traffic_sign_resnet18.pth`
- Load the trained model

---

### Notebook Exploration
Open the Jupyter notebook:
```bash
jupyter notebook notebooks/exploration.ipynb
```

Features:
- Auto‑train if model file is missing
- Load saved model
- Predict traffic sign classes
- Visualize predictions inline

---

## 🧪 Example Output
Training log:
```
Epoch 1/2 | Loss: 3.9790 | Acc: 0.00
Epoch 2/2 | Loss: 0.7091 | Acc: 1.00
💾 Model saved to models/traffic_sign_resnet18.pth
✅ Model loaded from models/traffic_sign_resnet18.pth
```

---

## 📈 Next Steps
- Add more synthetic or real traffic sign images (e.g., GTSRB dataset)
- Increase training epochs for better accuracy
- Add validation/test splits
- Expand unit tests in `tests/`
- Deploy as a Streamlit app for interactive use

---

## 🛠️ Tech Stack
- Python 3.11
- PyTorch & TorchVision
- OpenCV
- tqdm
- Jupyter Notebook
- pytest (for tests)

---

## 👩‍💻 Author
Developed by **Divya**  
AI/ML Developer | Full‑stack Python | Computer Vision Enthusiast
```

---

