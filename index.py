from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
from main import getPrediction

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    label = None
    confidence = None
    filename = None

    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            label, confidence = getPrediction(filepath)

    return render_template('index.html', label=label, confidence=confidence, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
