# from flask import Flask, render_template, request


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/hello', methods=['POST'])
# def hello():
#     name = request.form.get('name')
#     return render_template('hello.html', name=name)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.debug = True
    freezer.freeze()