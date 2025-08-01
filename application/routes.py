from flask import render_template, Flask, request, jsonify, redirect, url_for, flash
from urllib.parse import urlsplit
from application import app, db
from application.forms import LoginForm
import requests, os
from dotenv import load_dotenv
from flask_login import current_user, login_user, login_required, logout_user
import sqlalchemy as sa
from application.models import User
from application.forms import RegistrationForm

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

#== Index route ==
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home Page")

#== Profiles route ==
@app.route('/profiles.html')
def profiles():
    user = {'username': 'Mike'}
    return render_template('profiles.html', title="User Profiles", user=user)

#== Resources route ==
@app.route('/resources.html')
def resources():
    return render_template('resources.html', title="Resources")

#== Mindmap route ==
@app.route('/mindmap.html')
def mindmap():
    return render_template('mindmap.html', title="Mindmap")

#== Strategizing route ==
@app.route('/strategy.html')
@login_required
def strategy():
    return render_template('strategy.html', title="Strategizing")

#== Login route ==
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('resources')
        return redirect(url_for('index'))
    return render_template('login.html', title="Login", form=form)

#== Logout route ==
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


#== Registration route ==
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/get_response', methods=['POST'])
def get_response():
    userMessage = request.json.get('message')

    headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}

    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers=headers,
        json={
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': userMessage}],
            'max_tokens': 500
        }
    )

    chatbot_reply = response.json()['choices'][0]['message']['content']
    return jsonify({'response': chatbot_reply})
