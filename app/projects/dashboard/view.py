from flask import Blueprint, render_template, redirect, url_for, request, session
from app.services.firebase import DB, firestore
from app.projects.profil.view import login_required

dashboard_blueprint = Blueprint("dashboard", __name__, template_folder="templates")


@dashboard_blueprint.route("/dashboard")
@login_required
def dashboard():
    data = (
        DB.collection("Data Pengaduan")
        .order_by("tanggal", direction=firestore.Query.ASCENDING)
        .stream()
    )
    datas = []
    for d in data:
        us = d.to_dict()
        us["id"] = d.id
        datas.append(us)
    return render_template("dashboard.html", data=datas)


@dashboard_blueprint.route("/dashboard/<uid>")
@login_required
def lihat_data(uid):
    data = DB.collection("Data Pengaduan").document(uid).get().to_dict()
    return render_template("detail.html", data=data)


@dashboard_blueprint.route("/dashboard/hapus/<uid>")
@login_required
def hapus_berita(uid):
    DB.collection("Data Pengaduan").document(uid).delete()
    return redirect(url_for("dashboard.dashboard"))
