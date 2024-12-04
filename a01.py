from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>徐裕翔是帥哥!</p>"
if __name__ =="__main__":
    app.run()