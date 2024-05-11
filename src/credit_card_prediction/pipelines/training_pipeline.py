from src.credit_card_prediction.components.data_ingestion import DataIngestion

from src.credit_card_prediction.components.data_transformation import DataTransformation
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from src.credit_card_prediction.components.model_trainer import ModelTrainer

#from src.DimondPricePrediction.components.model_evaluation import ModelEvaluation


import os
import sys
from src.credit_card_prediction.logger import logging
from src.credit_card_prediction.exception import customexception
import pandas as pd

obj=DataIngestion()

train_data_path,test_data_path=obj.initiate_data_ingestion()

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)


model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)


#model_eval_obj = ModelEvaluation()
#model_eval_obj.initiate_model_evaluation(train_arr,test_arr)