from flask import Flask, request, render_template, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)
message_count = 0

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100))
    content = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    messages = Message.query.all()
    return render_template('index2.html', messages=messages)

@app.route('/send', methods=['POST'])
def send_message():
    message_content = request.form['message']
    new_message = Message(sender="user", content=message_content)
    with app.app_context():
        db.session.add(new_message)
        db.session.commit()
 
    # return redirect(url_for('index2'))
    return redirect(url_for('index'))
@app.route('/send2', methods=['POST'])
def send_message2():
    message_content = request.form['message']
    new_message = Message(sender="user2", content=message_content)
    with app.app_context():
        db.session.add(new_message)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/admin_reply', methods=['POST'])
def admin_reply():
    message_content = request.form['message']
    new_message = Message(sender="admin", content=message_content)
    with app.app_context():
        db.session.add(new_message)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
