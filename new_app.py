### Integrate HTML With Flask
### HTTP verb GET And POST
from flask import Flask,redirect,url_for,render_template,request

import pickle
import pandas as pd


app=Flask(__name__)

with open(r'D:\Flask_practice\model_pickle',"rb") as k:
    mk = pickle.load(k)


### Result checker submit html page
@app.route('/submit',methods=['GET' , 'POST'])
def submit():
    if request.method== 'POST':
        ok_json  = request.json

        prediction_pt = mk.predict(pd.DataFrame(ok_json , index=[0]))

        if prediction_pt == 0:
            return 'low'
        elif prediction_pt == 1:
            return 'medium'
        else:
            return 'high'




if __name__=='__main__':
    app.run(debug=True)