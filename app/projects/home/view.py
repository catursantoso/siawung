from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from app.services.firebase import DB

home_blueprint = Blueprint("home", __name__, template_folder="templates")


@home_blueprint.route("/")
@home_blueprint.route("/home", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {
            "nama": request.form["nama"],
            "jenis_kelamin": request.form["jenis_kelamin"],
            "pekerjaan": request.form["pekerjaan"],
            "alamat": request.form["alamat"],
            "email": request.form["email"],
            "medsos": request.form["medsos"],
            "nomor": request.form["nomor"],
            "pengaduan": request.form["pengaduan"],
            "tanggal": datetime.utcnow().strftime("%m/%d/%Y"),
        }
        DB.collection("Data Pengaduan").document().set(data)
        return redirect(url_for("home.index"))
    return render_template("index.html")
