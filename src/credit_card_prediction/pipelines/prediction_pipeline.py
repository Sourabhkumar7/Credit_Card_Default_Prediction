import os
import sys
import pandas as pd
from src.credit_card_prediction.exception import customexception
from src.credit_card_prediction.logger import logging
from src.credit_card_prediction.utils.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")
            
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            
            scaled_data=preprocessor.transform(features)
            
            pred=model.predict(scaled_data)
            
            return pred
            
            
        
        except Exception as e:
            raise customexception(e,sys)
    
    
    
class CustomData:
    def __init__(self, limit_bal, sex, education, marriage, age, pay_0,
                 pay_2, pay_3, pay_4, pay_5, pay_6, bill_amt1, bill_amt2,
                 bill_amt3, bill_amt4, bill_amt5, bill_amt6, pay_amt1,
                 pay_amt2, pay_amt3, pay_amt4, pay_amt5, pay_amt6):
        
        self.limit_bal = limit_bal
        self.sex = sex
        self.education = education
        self.marriage = marriage
        self.age = age
        self.pay_0 = pay_0
        self.pay_2 = pay_2
        self.pay_3 = pay_3
        self.pay_4 = pay_4
        self.pay_5 = pay_5
        self.pay_6 = pay_6
        self.bill_amt1 = bill_amt1
        self.bill_amt2 = bill_amt2
        self.bill_amt3 = bill_amt3
        self.bill_amt4 = bill_amt4
        self.bill_amt5 = bill_amt5
        self.bill_amt6 = bill_amt6
        self.pay_amt1 = pay_amt1
        self.pay_amt2 = pay_amt2
        self.pay_amt3 = pay_amt3
        self.pay_amt4 = pay_amt4
        self.pay_amt5 = pay_amt5
        self.pay_amt6 = pay_amt6
            
                
    def get_data_as_dataframe(self):
            try:
                custom_data_input_dict = {
            'LIMIT_BAL': [self.limit_bal],
            'SEX': [self.sex],
            'EDUCATION': [self.education],
            'MARRIAGE': [self.marriage],
            'AGE': [self.age],
            'PAY_0': [self.pay_0],
            'PAY_2': [self.pay_2],
            'PAY_3': [self.pay_3],
            'PAY_4': [self.pay_4],
            'PAY_5': [self.pay_5],
            'PAY_6': [self.pay_6],
            'BILL_AMT1': [self.bill_amt1],
            'BILL_AMT2': [self.bill_amt2],
            'BILL_AMT3': [self.bill_amt3],
            'BILL_AMT4': [self.bill_amt4],
            'BILL_AMT5': [self.bill_amt5],
            'BILL_AMT6': [self.bill_amt6],
            'PAY_AMT1': [self.pay_amt1],
            'PAY_AMT2': [self.pay_amt2],
            'PAY_AMT3': [self.pay_amt3],
            'PAY_AMT4': [self.pay_amt4],
            'PAY_AMT5': [self.pay_amt5],
            'PAY_AMT6': [self.pay_amt6]
                }
                df = pd.DataFrame(custom_data_input_dict)
                logging.info('Dataframe Gathered')
                return df
            except Exception as e:
                logging.info('Exception Occured in prediction pipeline')
                raise customexception(e,sys)
            
 