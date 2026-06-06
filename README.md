# 🔍 Computer Vision for Industrial Quality Control: Clamp Defect Detection using YOLOv8

This repository features an end-to-end Computer Vision project designed to automate quality control in manufacturing environments. Utilizing the **YOLOv8** architecture, the model accurately detects, localizes, and classifies industrial clamps in real-time into two categories: functional (`pinza_apta`) and defective (`pinza_defectuosa`).

Developed as a core portfolio project during my Data Science & Artificial Intelligence Bootcamp.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.x
* **Core Framework:** Ultralytics YOLOv8
* **Training Environment:** Google Colab (GPU Accelerated)
* **Dataset Management & Annotations:** Roboflow (Project: `MVP_Pinzas_Feria`)

## 📊 Model Performance & Evaluation
The model was evaluated using an independent test set, showcasing robust metrics ready for industrial deployment constraints:

| Metric | Value |
| :--- | :--- |
| **mAP@50** (Overall) | **92.1%** |
| **Precision** | **97.2%** |
| **Recall** | **94.7%** |
| **F1-Score** | **95.9%** |

### Per-Class Accuracy (mAP@50)
* **`pinza_apta` (Functional):** 100%
* **`pinza_defectuosa` (Defective):** 92.0%

> 💡 **Key Insight:** The model achieves a near-perfect precision rate (97.2%), meaning false positives are minimized—a critical requirement in quality assurance pipelines to avoid discarding flawless components.

---

## ⚙️ Training Configuration (`args.yaml`)
To ensure full reproducibility, the training process adhered strictly to the parameters documented in the `args.yaml` file:

* **Base Weights:** `yolov8s.pt` (YOLOv8 Small - selected for its optimal trade-off between inference speed and accuracy on small defects).
* **Task Mode:** Object Detection (`task: detect`, `mode: train`).
* **Input Resolution (`imgsz`):** 640x640 pixels.
* **Epochs:** 50.
* **Batch Size:** 16.
* **Data Augmentation:** Advanced techniques such as Mosaic (1.0) and horizontal flips (`fliplr: 0.5`) were applied to increase model resilience against variations in lighting, rotation, and camera placement on the factory floor.

---

## 📁 Repository Structure
While the full training imagery dataset remains private due to platform license constraints, this repository provides a fully functional testing environment:

```text
├── data/
│   ├── sample_images/     # Raw images to test model inference
│   └── data.yaml          # Dataset class definitions
├── models/
│   └── best.pt            # Final trained model weights ready for production
├── src/
│   └── predict.py         # Custom Python script for inference pipelines
└── args.yaml              # Original hyperparameters file