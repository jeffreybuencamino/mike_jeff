from flask import render_template, Flask, request, jsonify
from application import app
from application.forms import LoginForm
import requests

API_KEY = 'Your OPENAI API Key'  # Replace with your actual OpenAI API key
#== Index route ==
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mike'}
    return render_template('index.html', title="Home Page", user=user)

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
def strategy():
    return render_template('strategy.html', title="Strategizing")

#== Login route ==
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

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
