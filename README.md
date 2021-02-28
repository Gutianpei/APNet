# Person Re-identification via Attention Pyramid (APNet)
The official PyTorch code implementation for TIP20' Submission: "Person Re-identification via Attention Pyramid"

This repo only contains channel-wise attention(SE-Layer) implementation, to reproduce the result of spatial attention in our paper, please refer to [RGA-S](https://github.com/microsoft/Relation-Aware-Global-Attention-Networks) by Microsoft and simply change the attention agent. We also want to thank FastReid which is the codebase of our implementation.

## Requirements
- Python 3.6+
- PyTorch 1.5+
- CUDA 10.0+

Configuration other than the above setting is untested and we recommend to follow our setting.

To build all the dependency, please follow the instruction below.
```
conda create -n apnet python=3.7 -y
conda activate apnet
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 -f https://download.pytorch.org/whl/torch_stable.html
```
## Datasets
### Downloading
- Market-1501
- DukeMTMC-reID 
- MSMT17
### Preparation
After downloading the datasets above, move them to the `datasets/` folder in the project root directory, and rename dataset folders to 'market1501', 'duke' and 'msmt17' respectively. I.e., the `datasets/` folder should be organized as:
```
|-- market1501
    |-- bounding_box_train
    |-- bounding_box_test
    |-- ...
|-- duke
    |-- bounding_box_train
    |-- bounding_box_test
    |-- ...
|-- msmt17
    |-- bounding_box_train
    |-- bounding_box_test
    |-- ...
```

## Usage
### Training
```
bash demo.sh
```
### Evaluation
```
python eval.py
```
