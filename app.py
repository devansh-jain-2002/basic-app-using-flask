from flask import Flask, render_template , request
studentData={'210321':{'name':'Devansh Jain','branch':'CSE','gender':'male'},
'210323':{'name':'Dummy1','branch':'CE','gender':'male'},
'210325':{'name':'Dummy2','branch':'EE','gender':'female'},
'210329':{'name':'Dummy3','branch':'PHY','gender':'male'}}
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/show/<rollno>')
def details(rollno):
    return f'Hi {rollno}'
@app.route('/student_search/',methods=['GET'])
def login():
    roll=request.args.get('rollno')
    if roll in studentData:
        stu = studentData[roll]
        return f'Name: {stu["name"]}<br>Branch: {stu["branch"]}<br>Gender: {stu["gender"]}<br>'
    else:
        return 'Invalid Roll No'
if __name__=='__main__':
    app.run(debug=True)
