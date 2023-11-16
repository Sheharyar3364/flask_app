# run.py

from myapp import create_app
from myapp.extensions import db

app = create_app()

if __name__ == '__main__':
    # Create tables and run the app
    with app.app_context():
        db.create_all()
    app.run(debug=True)
