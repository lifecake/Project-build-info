# Install
Python:
Install Python 3.x. https://www.python.org/downloads/.

Flask:
Install Flask. pip install Flask, if using Mac, after installing Python 3 you can use pip3 install Flask.

Bootstrap:
Install bootstrap. pip install flask-bootstrap.

# RUN
export FLASK_APP=flaskr

export FLASK_ENV=development

flask init-db # init db will drop all tables.Please backup db or edit sql.

flask run --host=0.0.0.0 # This tells your operating system to listen on all public IPs.
