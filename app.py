from flask import Flask, render_template
import json
import random
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route('/')
@app.route('/member')
def show_member():
    json_path = os.path.join(app.root_path, 'crew.json')
    with open(json_path, encoding='utf-8') as f:
        crew = json.load(f)
    member = random.choice(crew)
    return render_template('member.html', member=member)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')