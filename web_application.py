from application import app, db
from application.models import User, Post
import sqlalchemy as sa
import sqlalchemy.orm as so

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post,
        'sa': sa,
        'so': so
    }

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)