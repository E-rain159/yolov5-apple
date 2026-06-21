# YOLOv5 项目说明

这是一个基于 YOLOv5 的目标检测项目仓库，可用于本地推理、模型训练、效果验证和模型导出。

本项目重点面向苹果目标识别，能够对图片、视频或摄像头画面中的苹果进行检测，也可以继续扩展到其他类别目标。

仓库中包含 YOLOv5 的常用脚本和目录：

- `detect.py`：目标检测推理
- `train.py`：模型训练
- `val.py`：模型验证
- `export.py`：模型导出
- `models/`：模型配置文件
- `data/`：数据集配置文件
- `utils/`：工具函数
- `runs/`：训练和推理结果输出目录

## 项目特点

- 支持苹果目标识别与检测
- 支持图片、视频、摄像头、文件夹和流媒体推理
- 支持自定义数据集训练
- 支持模型验证与导出
- 基于 PyTorch 实现

## 环境要求

- Python 3.8 及以上
- PyTorch 1.8 及以上
- 可选 CUDA，建议在训练或 GPU 推理时使用

## 安装方法

克隆仓库并安装依赖：

```bash
git clone <你的仓库地址>
cd yolov5-master
pip install -r requirements.txt
```

如果项目已经在本地，只需要进入目录后执行：

```bash
pip install -r requirements.txt
```

## 快速开始

### 1. 图片检测

```bash
python detect.py --weights yolov5s.pt --source 92.jpg
```

如果你已经训练了苹果识别模型，可以将 `--weights` 替换为你自己的苹果检测权重文件。

### 2. 摄像头检测

```bash
python detect.py --weights yolov5s.pt --source 0
```

### 3. 自定义数据集训练

```bash
python train.py --data data/custom.yaml --weights yolov5s.pt --img 640 --epochs 100
```

请根据自己的数据集修改 `data/custom.yaml`。

### 4. 模型验证

```bash
python val.py --weights yolov5s.pt --data data/coco128.yaml --img 640
```

### 5. 导出 ONNX 模型

```bash
python export.py --weights yolov5s.pt --include onnx
```

## 项目结构

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

## 使用说明

- 项目当前可以作为苹果识别项目的基础仓库使用
- `runs/` 通常保存推理或训练生成的结果，不建议上传过多实验输出到 GitHub
- `yolov5s.pt` 是预训练权重文件
- 如果后续加入自己的大规模数据集，建议不要直接上传原始数据到 GitHub

## 上传到 GitHub

修改完成后，可以执行以下命令重新提交并推送：

```bash
git add README.md
git commit -m "Rewrite README in Chinese"
git push -u origin main
```

如果推送时仍然出现连接中断问题，可以先执行：

```bash
git config --global http.version HTTP/1.1
git push -u origin main
```

## 许可证

本项目基于 YOLOv5 代码结构整理和使用，原始许可证请查看仓库中的 [LICENSE](LICENSE) 文件。
