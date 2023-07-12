from flask import Flask, render_template

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='development'
)

@app.route('/')
def home():
    return render_template('partials/inicio.html')
    

# @app.route('/casa')
# def casa():
#     return render_template('partials/nabvar.html')

HOST = 'localhost'
PORT = 4000
DEBUG = True

if(__name__ == '__main__'):
    app.run(HOST, PORT, DEBUG)
