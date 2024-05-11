    
from src.credit_card_prediction.pipelines.prediction_pipeline import CustomData,PredictPipeline

from flask import Flask,request,render_template,jsonify


app=Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    
    else:
        data=CustomData(
            
            
        limit_bal = request.form.get("LIMIT_BAL"),
        sex = request.form.get("SEX"),
        education = request.form.get("EDUCATION"),
        marriage = request.form.get("MARRIAGE"),
        age = request.form.get("AGE"),
        pay_0 = request.form.get("PAY_0"),
        pay_2 = request.form.get("PAY_2"),
        pay_3 = request.form.get("PAY_3"),
        pay_4 = request.form.get("PAY_4"),
        pay_5 = request.form.get("PAY_5"),
        pay_6 = request.form.get("PAY_6"),
        bill_amt1 = request.form.get("BILL_AMT1"),
        bill_amt2 = request.form.get("BILL_AMT2"),
        bill_amt3 = request.form.get("BILL_AMT3"),
        bill_amt4 = request.form.get("BILL_AMT4"),
        bill_amt5 = request.form.get("BILL_AMT5"),
        bill_amt6 = request.form.get("BILL_AMT6"),
        pay_amt1 = request.form.get("PAY_AMT1"),
        pay_amt2 = request.form.get("PAY_AMT2"),
        pay_amt3 = request.form.get("PAY_AMT3"),
        pay_amt4 = request.form.get("PAY_AMT4"),
        pay_amt5 = request.form.get("PAY_AMT5"),
        pay_amt6 = request.form.get("PAY_AMT6")
        )
         #this is my final data
        final_data=data.get_data_as_dataframe()
        
        predict_pipeline=PredictPipeline()
        
        pred=predict_pipeline.predict(final_data)
        
        result=round(pred[0],2)
        if result==1:
            result="The user is default from next month"
        else:
            result="The user is not default"
        
        return render_template("result.html",final_result=result)

#execution begin
if __name__ == '__main__':
    app.run(debug=True,port=5000)
    #app.run(host="0.0.0.0",port=8080)