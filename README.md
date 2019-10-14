# Piru compose

This repository aims to be a collaborative project to create Machine Learning music composer based on a dataset of existing tracks

## Current stage
nothingness

## How to contribute
At this stage contributions would ideally take the form of jupyter notebooks

### Install anaconda & dependencies
See https://docs.anaconda.com/anaconda/install/


Create a conda conda virtual default environement, activate it and install dependencies 

```
> conda create --name pirucompose python=3.7 anaconda
> conda activate pirucompose
> pip install -r requirements.txt
```

### Prepare datasets
Clone this repository and download the following dataset in the data directory:
https://drive.google.com/open?id=1HWlsQZWir3c4cePo0LFP-knOqBTtgiKI

Unzip them in the data directory

Add pirucompose environement to jupyter 
```
> python -m ipykernel install --user --name pirucompose --display-name "PiruCompose"
```

Start the jupyter notebook engine
```
> jupyter notebook
```
