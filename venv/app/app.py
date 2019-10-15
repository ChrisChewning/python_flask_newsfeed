# app.py
# from flask import Flask, jsonify  #import modules
# from flask_bootstrap import Bootstrap
# from newsfeed import getWaPo


# app = Flask(__name__) #instatiate class
# Bootstrap(app)

# @app.route('/')  #decorator defines the URI
# def index():
#     return jsonify(Products=getWaPo())
# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=8001)

# {% extends "bootstrap/base.html" %}
# {% block title %}This is an example page{% endblock %}

# {% block navbar %}
# <div class="navbar navbar-fixed-top">
#   <!-- ... -->
# </div>
# {% endblock %}

# {% block content %}
#   <h1>Hello, Bootstrap</h1>
# {% endblock %}