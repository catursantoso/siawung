from app import app

from app.projects.home.view import home_blueprint
from app.projects.profil.view import profil_blueprint
from app.projects.dashboard.view import dashboard_blueprint
from app.projects.berita.view import berita_blueprint

app.register_blueprint(home_blueprint, url_prefix="/")
app.register_blueprint(profil_blueprint, url_prefix="/")
app.register_blueprint(dashboard_blueprint, url_prefix="/")
app.register_blueprint(berita_blueprint, url_prefix="/")
