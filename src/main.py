import config
import flask

import view


app = flask.Flask(__name__)
app.config.from_object(config.Configuration)
app.register_blueprint(view.base_bp)
app.run()
