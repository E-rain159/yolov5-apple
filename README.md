# YOLOv5 Project

This repository contains a YOLOv5-based object detection project for local inference, training, validation, and model export.

It includes the common YOLOv5 entry scripts and folders:

- `detect.py`: run object detection inference
- `train.py`: train a model
- `val.py`: validate a model
- `export.py`: export a model
- `models/`: model configs
- `data/`: dataset configs
- `utils/`: utility functions
- `runs/`: training and inference outputs

## Features

- Image, video, webcam, folder, and stream inference
- Custom dataset training
- Model validation and export
- PyTorch-based implementation

## Requirements

- Python 3.8 or newer
- PyTorch 1.8 or newer
- CUDA is optional but recommended for GPU training and inference

## Installation

Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd yolov5-master
pip install -r requirements.txt
```

If the project is already on your machine, just enter the folder and run:

```bash
pip install -r requirements.txt
```

## Quick Start

### Run detection on an image

```bash
python detect.py --weights yolov5s.pt --source 92.jpg
```

### Run detection with a webcam

```bash
python detect.py --weights yolov5s.pt --source 0
```

### Train on a custom dataset

```bash
python train.py --data data/custom.yaml --weights yolov5s.pt --img 640 --epochs 100
```

Update `data/custom.yaml` to match your dataset.

### Validate a model

```bash
python val.py --weights yolov5s.pt --data data/coco128.yaml --img 640
```

### Export to ONNX

```bash
python export.py --weights yolov5s.pt --include onnx
```

## Project Structure

```text
yolov5-master/
|- data/
|- models/
|- utils/
|- classify/
|- segment/
|- runs/
|- detect.py
|- train.py
|- val.py
|- export.py
|- requirements.txt
```

## Notes

- `runs/` usually contains generated experiment output and should not grow too large in GitHub
- `yolov5s.pt` is a pretrained weight file
- Large raw datasets should not be uploaded directly to GitHub

## Upload to GitHub

After updating the README, commit and push again:

```bash
git add README.md
git commit -m "Rewrite README"
git push -u origin main
```

If HTTPS push still fails because the connection resets, try:

```bash
git config --global http.version HTTP/1.1
git push -u origin main
```

## License

This project is based on the YOLOv5 code structure. See [LICENSE](LICENSE) for the original license information.
