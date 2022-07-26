from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app.services.firebase import DB
from functools import wraps

profil_blueprint = Blueprint(
    "profil_desa", __name__, template_folder="templates", static_folder="static_profil"
)


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user" in session:
            return f(*args, **kwargs)
        else:
            flash("Maaf anda belum login", "warning")
            return redirect(url_for("profil_desa.profil"))

    return wrapper


@profil_blueprint.route("/profil_desa")
def profil():
    return render_template("profil.html")


@profil_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("dashboard.dashboard"))
    if request.method == "POST":
        data = {
            "username": request.form["username"],
            "sandi": request.form["sandi"],
        }

        users = (
            DB.collection("admin").where("username", "==", data["username"]).stream()
        )
        user = {}
        for us in users:
            user = us.to_dict()
        if user and check_password_hash(user["sandi"], data["sandi"]):
            # login_user(user)
            session["user"] = user
            session["userId"] = us.id
            # flash('Anda berhasil login', 'success')
            return redirect(url_for("dashboard.dashboard"))
        else:
            flash("Maaf, anda gagal login", "danger")
    return render_template("profil.html")


@profil_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if "user" in session:
        return redirect(url_for("dashboard.dashboard"))
    if request.method == "POST":
        data = {
            "username": request.form["username"],
            "sandi": request.form["sandi"],
        }

        data["sandi"] = generate_password_hash(request.form["sandi"], "sha256")
        DB.collection("admin").document().set(data)
        flash("Sudah Terdaftar")
        return redirect(url_for("profil_desa.profil"))
    return render_template("profil.html")


@profil_blueprint.route("/logout")
@login_required
def logout():
    session.clear()
    return render_template("profil.html")
