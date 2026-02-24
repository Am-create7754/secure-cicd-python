from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure CI/CD Pipeline with Python!"

if __name__ == "__main__":
    app.run(port=5000)