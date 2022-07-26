from flask import Flask

app = Flask(__name__, template_folder="projects")
app.secret_key = "websitedesasiawungbykknunhas108"

from app.projects import main_views
