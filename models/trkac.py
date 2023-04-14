from db import db


class TrkacModel(db.Model):
    __tablename__ = "trkacs"

    #id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(80), unique=False, nullable=False)
    #store_id = db.Column(db.Integer(), db.ForeignKey("stores.id"), nullable=False)


    id_trkac = db.Column(db.Integer, primary_key=True)
    bib = db.Column(db.String(80), unique=True, nullable=False)
    tagCode = db.Column(db.String(80), unique=False, nullable=False)
    imePrezime = db.Column(db.String(80), unique=False, nullable=False)
    godinaRodjenja = db.Column(db.String(80), unique=False, nullable=False)
    mestoStanovanja = db.Column(db.String(80), unique=False, nullable=False)
    drzava = db.Column(db.String(80), unique=False, nullable=False)
    klub = db.Column(db.String(80), unique=False, nullable=False)
    starosnaKategorija = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    smsBroj = db.Column(db.String(80), unique=False, nullable=False)
    storno = db.Column(db.String(80), unique=False, nullable=False)  # treba da bude bollean ili int
    #trka_id = db.Column(db.Integer(), db.ForeignKey("trkas.id"), nullable=False)

    #manifestacija_id = db.Column(db.Integer(), db.ForeignKey("manifestacijas.id_manifestacija"), nullable=False)
    #manifestacija = db.relationship("ManifestacijaModel", back_populates="trkacs")
    #trkas = db.relationship("TrkaModel", back_populates="trkacs") #, secondary="trkas_trkacs")

    trka_id = db.Column(db.Integer, db.ForeignKey("trkas.id_trka"), unique=False, nullable=False)
    trka = db.relationship("TrkaModel", back_populates="trkacs")


    #store_id = db.Column(db.Integer(), db.ForeignKey("stores.id"), nullable=False)

    #store_id = db.Column(
    #    db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False
    #)
    #store = db.relationship("StoreModel", back_populates="items")