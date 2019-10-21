from flask import Flask
app=Flask(__name__)
@app.route('/')
def hellowroldhander():
    return 'HEllo world from Flask & VAGRANT'

if __name__ == "__main__":
    app.run(host="0.0.0.0")

