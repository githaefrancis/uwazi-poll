from flask import render_template
from . import main

@main.route('/')
def index():
  return render_template('main/index.html')


@main.route('/student')
def student():
  return render_template('main/student.html',title='Student')  