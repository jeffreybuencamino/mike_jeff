from flask import render_template
from application import app
from application.forms import LoginForm

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