from flask import Flask, render_template
from routes.chat import chat_bp
from routes.history import history_bp
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

app.register_blueprint(chat_bp)
app.register_blueprint(history_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    from db import init_db
    init_db()
    app.run(debug=True)