from app import app
from flask import render_template
import forms
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.Submit()
    message = form.data
    os.system(message.data)
    return render_template('index.html', form=form)

