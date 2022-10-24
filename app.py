import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)


if __name__ == '__main__':
    print("ASD")
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))