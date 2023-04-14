from db import db


class AndroidModel(db.Model):
    __tablename__ = "androids"

    id_android = db.Column(db.Integer, primary_key=True)
    bib_android = db.Column(db.String(150), unique=True, nullable=False)
    pozicija_android = db.Column(db.String(80), unique=True, nullable=False)
    tag_code_android = db.Column(db.String(80), unique=True, nullable=False)
    vreme_sistemsko_android = db.Column(db.String(80), unique=True, nullable=False)
    storno_android = db.Column(db.String(80), unique=True, nullable=False)

    trka_id = db.Column(db.Integer, db.ForeignKey("trkas.id_trka"), unique=False, nullable=False)
    trka = db.relationship("TrkaModel", back_populates="androids")
""""
    trka_id = db.Column(db.Integer, db.ForeignKey("trkas.id_trka"), unique=False, nullable=False)
    trka = db.relationship("TrkaModel", back_populates="trkacs")

    manifestacija_id = db.Column(
        db.Integer, db.ForeignKey("manifestacijas.id_manifestacija"), unique=False, nullable=False
    ) # mora zbog povezivanja sa manifestacijom
    manifestacija = db.relationship("ManifestacijaModel", back_populates="trkas") #items = trkas
"""