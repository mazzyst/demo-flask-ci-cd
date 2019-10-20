from flask import Flask
app=Flask(__name__)
@app.route('/')
def hellowroldhander():
    return 'HEllo world from Flask & VAGRANT'
