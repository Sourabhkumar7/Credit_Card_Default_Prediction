# This is my end to end credit card default prediction project.......
Welcome to my credit card default prediction project! In this end-to-end endeavor, I tackled the challenging task of forecasting credit card default. The project involves cleaning and refining the diamond dataset to ensure its accuracy. I visualized and analyzed the data, drwaing meaningful conclusions to gain valuable insights. The predictive power comes from a sophisticated machine learning algorithm, providing precise credit card default prediction predictions. Taking it a step further, I've seamlessly deployed the model on AWS for real-world accessibility and scalability.

Key Steps
Data Cleaning: I meticulously cleaned and refined the credit card dataset, eliminating messy and unwanted data.
Exploratory Data Analysis (EDA): Visualized and analyzed the data to draw insightful conclusions, shedding light on essential patterns.
Machine Learning Model: Developed and fine-tuned a supervised learning algorithm to predict credit card default prediction accurately.
AWS Deployment: Seamlessly deployed the predictive model on AWS, ensuring accessibility and scalability for practical applications.













## Git
git log
git branch
git checkout ...
git status
after commit ,it generete a each hash key of that particular thing






## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### local cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/sourabh/fsdsmendtoend.mlflow \
MLFLOW_TRACKING_USERNAME=sourabh \
MLFLOW_TRACKING_PASSWORD=3c2c8cd1436ad32b510cfdd84944a528ba4fb650 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/sourabh/fsdsmendtoend.mlflow

export MLFLOW_TRACKING_USERNAME=sourabh

export MLFLOW_TRACKING_PASSWORD=3c2c8cd1436ad32b510cfdd84944a528ba4fb650

```


### DVC cmd
- dvc init
- dvc repro
- dvc dag
