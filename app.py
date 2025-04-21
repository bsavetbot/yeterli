from flask import Flask

app = Flask(_ _name_ _)

@app.route('/')
def home():
    return "Sistem Rotası çalışıyor!"

if _ _name_ _ == '_ _main_ _  ':
    app.run()