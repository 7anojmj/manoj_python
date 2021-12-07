from flask import Flask, request, render_template
import ans01
import shutil
import os

app = Flask(__name__)

if not os.path.exists('stamp_dir'):
    os.makedirs('stamp_dir')
if not os.path.exists('sign_dir'):
    os.makedirs('sign_dir')
shutil.rmtree('sign_dir')
shutil.rmtree('stamp_dir')
if not os.path.exists('stamp_dir'):
    os.makedirs('stamp_dir')
if not os.path.exists('sign_dir'):
    os.makedirs('sign_dir')


@app.route('/', methods=['GET', 'POST'])
def f():
    if request.method == "POST":
        # if not os.path.isdir(app.config['UPLOAD_FOLDER']):
        #   os.mkdir(app.config['UPLOAD_FOLDER'])

        f1 = request.files["upload_1"]
        if f1:
            path1 = os.path.join('stamp_dir', f1.filename)
            f1.save(path1)
        # print(path1)


        f2 = request.files["upload_2"]
        if f2:
            path2 = os.path.join('sign_dir', f2.filename)
            f2.save(path2)
        # print(path2)
        ran = request.form.get("correct")

        # print(path1)
        if request.form["action"] == "Generate transcript(s)":
            if len(os.listdir('stamp_dir')) > 0 and len(os.listdir('sign_dir')) :
                result = ans01.list_generation(ran,path1, path2)
            else   :
                result = ans01.list_generation(ran,'', '')


        # print(os.listdir('sign_dir'))
    return render_template('view.html')


if __name__ == '__main__':
    app.run(debug=True)




