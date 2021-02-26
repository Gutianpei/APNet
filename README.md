# APNet
Official code for TIP submission "Person Re-identification via Attention Pyramid"

# Person Re-identification via Attention Pyramid (APNet)
This repo contains official PyTorch code implementation for TIP20' Submission: "Person Re-identification via Attention Pyramid"

## Requirements
- Python 3.6+
- PyTorch 1.7

To install all python packages, please run the following command:
```
pip install -r requirements.txt
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
