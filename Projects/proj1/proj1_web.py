from flask import Flask,request,render_template
from proj1 import generate_marksheet, concise_marksheet, Send_email
import pandas as pd
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "sample_input"
@app.route('/', methods=['GET', 'POST'])
def f():

    if request.method == "POST":
        #if not os.path.isdir(app.config['UPLOAD_FOLDER']):
         #   os.mkdir(app.config['UPLOAD_FOLDER'])

        f1 = request.files["upload_1"]
        path1 = os.path.join(app.config['UPLOAD_FOLDER'], f1.filename)
        f1.save(f1.filename)
        f2 = request.files["upload_2"]
        path2 = os.path.join(app.config['UPLOAD_FOLDER'], f2.filename)
        f2.save(f2.filename)
        pos = request.form.get("correct")
        neg = request.form.get("wrong")
        if request.form["action"] == "Generate Roll number wise Marksheet":
            result = generate_marksheet(path1, path2, pos, neg)
        if request.form["action"] == "Generate Concise Marksheet with Roll Num, Obtained Marks, marks after negative":
            result = concise_marksheet(path1, path2, pos, neg)
        if request.form["action"] == "Send Email":
            result = Send_email(path1, path2, pos, neg)
    return render_template('view.html')
   
if __name__ == '__main__':
    app.run(debug=True)

	    
			
		
			