from flask import Blueprint, render_template, request, redirect, url_for
from app.services.firebase import DB, firestore
from datetime import datetime
from app.projects.profil.view import login_required

berita_blueprint = Blueprint(
    "berita", __name__, template_folder="templates", static_folder="static_berita"
)


@berita_blueprint.route("/berita")
def berita():
    data = (
        DB.collection("Berita")
        .order_by("tanggal", direction=firestore.Query.DESCENDING)
        .stream()
    )
    datas = []
    for dt in data:
        d = dt.to_dict()
        d["id"] = dt.id
        datas.append(d)

    return render_template("berita.html", data=datas)


@berita_blueprint.route("/berita/buat_berita", methods=["GET", "POST"])
def add_berita():
    if request.method == "POST":
        data = {
            "judul": request.form["judul"],
            "deskripsi": request.form["deskripsi"],
            "penulis": request.form["penulis"],
            "isi": request.form["isi"],
            "tanggal": datetime.utcnow().strftime("%m/%d/%Y"),
        }
        DB.collection("Berita").document().set(data)
        return redirect(url_for("berita.berita"))
    return render_template("berita.html")


@berita_blueprint.route("/berita/<uid>", methods=["GET", "POST"])
def konten_berita(uid):
    data = DB.collection("Berita").document(uid).get().to_dict()
    if request.method == "POST":
        datas = {
            "judul": request.form["judul"],
            "deskripsi": request.form["deskripsi"],
            "penulis": request.form["penulis"],
            "isi": request.form["isi"],
        }
        DB.collection("Berita").document(uid).set(datas, merge=True)
        return redirect(url_for("berita.berita"))
    user = DB.collection("Berita").document(uid).get().to_dict()
    user["id"] = uid
    return render_template("konten_berita.html", data=data, user=user)


@berita_blueprint.route("/berita/hapus/<uid>")
@login_required
def hapus_berita(uid):
    DB.collection("Berita").document(uid).delete()
    return redirect(url_for("berita.berita"))
