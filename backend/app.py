import os

from flask import Flask, send_from_directory

def create_app(settings='settings.development'):
    # https://stackoverflow.com/questions/47511303/setting-static-template-filepath-to-sibbling-parent-folder-in-flask
    # https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
    app = Flask(__name__, root_path=os.path.abspath("../"), static_url_path='/', static_folder='dist')
    app.config.from_object(settings)

    @app.route("/")
    def index():
        # https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
        return send_from_directory('dist', 'index.html')

    @app.route("/test")
    def test():
        return "<p>test</p>"

    return app