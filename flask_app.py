from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    input_text= ''
    if request.method == 'POST':
        input_text= request.form.get('in_text')

    input_text= input_text.upper()
    return render_template('index.html', up_text= input_text)

if __name__ == '__main__': 
   app.run(debug = True) 
