from flask import Flask, request, redirect, url_for, render_template
import random
import string

app = Flask(__name__)

# Global static token
STATIC_TOKEN = f"LEAK_ME_{''.join(random.choices(string.ascii_uppercase + string.digits, k=6))}"
comments = []

@app.before_request
def enforce_token():
    token = request.args.get('token')
    if token != STATIC_TOKEN:
        return redirect(url_for('index', token=STATIC_TOKEN))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment = request.form.get('comment', '')
        comments.append(comment)
        return redirect(url_for('index', token=STATIC_TOKEN))
    return render_template('index.html', comments=comments, token=STATIC_TOKEN)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
