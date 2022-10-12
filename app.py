from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def home():
    prompts = silly_story.prompts;
    return render_template('questions.html', prompts=prompts)


@app.get('/story')
def complete_story():
    answers = {}
    for key in request.args:
        answers[key] = request.args[key]
    print('answers:', answers)
    print('request.args: ', request.args)
    finished_story = silly_story.generate(answers)
    return render_template('results.html', finished_story=finished_story)