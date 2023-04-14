from db import db

class Negativni_poeniModel(db.Model):
    __tablename__ = "negativni_poenis"

    id_negativni = db.Column(db.Integer, primary_key=True)
    pozicija_negativni = db.Column(db.String(150), unique=True, nullable=False)
    broj_poena_negativni = db.Column(db.String(80), unique=True, nullable=False)
    kazna_sec_negativni = db.Column(db.String(80), unique=True, nullable=False)
    storno_negativni = db.Column(db.String(80), unique=True, nullable=False)

    trka_id = db.Column(db.Integer, db.ForeignKey("trkas.id_trka"), unique=False, nullable=False)
    trka = db.relationship("TrkaModel", back_populates="negativni_poenis")


"""
tabela negativni poeni
-id
-pozicija
-broj_poena
-kazna_sec
-storno

"""