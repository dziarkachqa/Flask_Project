#1. Create enviroment python -m venv venv
#2. Active enviroment .\venv\Scripts\activate
#3. Check Pycharm Interpreter(Add Interpriter, OK)
#4. Add file requirements.txt
#(add here framework/module == version)
#5. Run requirements file to install module:
#(optinal: pip install -U pip )
#pip install -r requirements.txt
#To publish:
#.gitignore: venv, .idea/, env, __py.cache__
#README.md\


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Skillo!'
