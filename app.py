from flask import Flask, request, render_template
from module import CheckerModule

app = Flask(__name__)
spell_check = CheckerModule()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/correct', methods=["POST"])
def correct():
    if request.method == 'POST':
        text = request.form['text']
        corrected_text, incorrect_words = spell_check.correct_spell(text)
        return render_template('index.html', corrected_text=corrected_text, incorrect_words=incorrect_words)

if __name__ == "__main__":
    app.run(debug=True)
