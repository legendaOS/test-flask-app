from flask import Flask, Blueprint

app = Flask(__name__)

from Router import router

app.register_blueprint(router, url_prefix = '/api')

app.run(port=25560, debug=False)