# Adenocarcinoma-Chest-Cancer-Classification-using-MLflow-DVC-AWS 
## MLOPS / DLOPS


*A Streamlit-based web application to classify chest CT scans for adenocarcinoma cancer detection using deep learning.*

---

## Overview

This project is a machine learning-powered web application built with Streamlit and TensorFlow to classify chest CT scan images as **Normal** or **Adenocarcinoma Cancer**. Deployed on AWS (EC2 via ECR) and optionally on Streamlit Community Cloud, it provides an intuitive interface for uploading images and viewing detailed prediction results, including probabilities and class indices.

### Live Demo
- **AWS Deployment**: [http://54.211.105.80:8501](http://54.211.105.80:8501)  
- **Streamlit Cloud**: [https://adenocarcinoma-cancer-detection.streamlit.app/](https://adenocarcinoma-cancer-detection.streamlit.app/)

---

## Features

- **Image Classification**: Upload a chest CT scan (JPG, JPEG, PNG) and get instant predictions.
- **Detailed Output**: View the final prediction, raw probabilities, and class index.
- **AWS Integration**: Model fetched from S3 or bundled in the container for robust deployment.
- **User-Friendly UI**: Built with Streamlit for a seamless experience.

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, TensorFlow, NumPy
- **Model**: Pre-trained Convolutional Neural Network (CNN)
- **AWS Services**: ECR (Docker hosting), EC2 (self-hosted runner), S3 (model storage)
- **CI/CD**: GitHub Actions
- **Containerization**: Docker

---


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml





## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtube.com/playlist?list=PLkz_y24mlSJZrqiZ4_cLUiP0CBN5wFmTb&si=zEp_C8zLHt1DzWKK)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI= \
MLFLOW_TRACKING_USERNAME= \
MLFLOW_TRACKING_PASSWORD= \
python script.py


Run this to export as env variables into the terminal:
export for mac/linux and set for windows...
```bash

export MLFLOW_TRACKING_URI=________

export MLFLOW_TRACKING_USERNAME=______

export MLFLOW_TRACKING_PASSWORD=__________
```




### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: __________

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = ___.com___

    ECR_REPOSITORY_NAME = simple-app


Note:-
app.py --> Work perfectly on localhost.
app_streamlit.py --> work perfectly on cloud server.
