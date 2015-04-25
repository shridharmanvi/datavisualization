from __future__ import division
from flask import Flask, jsonify,request, render_template, redirect, url_for, session
import clustering as c
from werkzeug import secure_filename


app=Flask(__name__)


@app.route('/')
def route():
    return 'Hey'

@app.route('/data',methods=['GET','POST'])
def data():
    #filename= 'f_name'
    #num_clu= 'n'
    if request.method== 'POST':
        #c.main(filename,num_clu)
        file = request.files['file']
        filename = secure_filename(file.filename)
        print filename
        file.save('./templates/' + filename)
        print 'Upload complete' 
        return render_template('base.html')

   
    return render_template('data.html')





if __name__== '__main__':
    app.run(host='0.0.0.0', port=80,debug='true')

