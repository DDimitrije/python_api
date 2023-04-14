#from db import db
from db import db


class CitacModel(db.Model):
    __tablename__ = "citacs"

    id_citac = db.Column(db.Integer, primary_key=True)
    bib_citac = db.Column(db.String(150), unique=True, nullable=False)
    ime_preziem_citac = db.Column(db.String(80), unique=True, nullable=False)
    age_group_citac = db.Column(db.String(80), unique=True, nullable=False)
    age_gun_time = db.Column(db.String(80), unique=True, nullable=False)
    age_net_time = db.Column(db.String(80), unique=True, nullable=False)
    age_storno = db.Column(db.String(80), unique=True, nullable=False)

    trka_id = db.Column(db.Integer, db.ForeignKey("trkas.id_trka"), unique=False, nullable=False)
    trka = db.relationship("TrkaModel", back_populates="citacs")
"""
tabela sa kineza
-id
-bib
-ime_preziem
-age_group
-gun_time
-net_time
-storno
"""