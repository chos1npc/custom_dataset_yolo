# Object detection on custom dataset
Course in NTU:computer vision practice with deep learning

## 📌 Overview
This repository contains scripts and reports related to object detection experiments using YOLOv8. The main tasks include implementing detection scripts, comparing performance, and visualizing results.

## 📂 Repository Structure
```bash
📦 project-root
├── 📜 hw1.sh              # Script to run object detection using YOLO
├── 📜 hw1_download.sh     # Script to download YOLO model checkpoints
├── 📜 hw1_61147050S.pdf   # Report detailing CNN-based and Transformer-based object detection
├── 📂 ultralytics/        # Directory containing the YOLO framework
```

## 🛠 Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `ultralytics` package for YOLO v8
- PyTorch
- OpenCV (for visualization)

### Setup
```bash
pip install ultralytics torch torchvision opencv-python
```

### 📥 Downloading Pretrained Models
To download pretrained YOLO models:
```bash
bash hw1_download.sh
```
This script downloads:
- `yolocheckpoint.pt` (checkpoint model)
- `yolopretrain.pt` (pretrained model)

### YOLOv8 Detection
### Custom Data Detection
1. Run `hw1_download.sh` to download the pretrained model and the trained checkpoint.
2. Execute `hw1.sh` with three parameters:
   - Input image path
   - Checkpoint path (downloaded model)
   - Output JSON file path
3. The output will be stored in `ultralytics/detect_json/` for reference.

### Training with Custom Data
1. Convert JSON annotations to YOLO format using:
   ```bash
   python txtrans.py
   ```
2. Organize the dataset according to `cvpdl.yaml`.
3. Run the training command:
   ```bash
   yolo detect train data=./ultralytics/datasets/cvpdl.yaml \
        model=yolov8m.yaml epochs=300 imgsz=640 pretrained=<pretrain_model>
   ```
   - `<pretrain_model>`: Path to the pretrained model.
   - `data`: Path to the dataset YAML file.



## 📊 Performance Comparison
A detailed comparison of YOLOv8 and DINO on object detection is provided in `hw1_61147050S.pdf`. Key metrics include:

| Model  | mAP@[50:5:95] | mAP@50 | mAP@75 | Small Objects | Medium Objects | Large Objects |
|--------|--------------|--------|--------|--------------|---------------|--------------|
| YOLOv8m | 0.4805 | 0.7578 | 0.5058 | 0.1557 | 0.3618 | 0.5859 |

## 🔗 References
- [📖 Ultralytics YOLOv8 Documentation](https://docs.ultralytics.com/usage/cfg/)
