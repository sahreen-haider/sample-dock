from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',  method=['GET'])
def welcome():
    return render_template('index.html')
    # return '<h>Hello, Welcome!</h>' 
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)