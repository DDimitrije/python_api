from db import db


class ManifestacijaModel(db.Model):
    __tablename__ = "manifestacijas"

    id_manifestacija = db.Column(db.Integer, primary_key=True)
    imeManifestacija = db.Column(db.String(150), unique=True, nullable=False)
    datum = db.Column(db.String(80), unique=True, nullable=False)
    vremeStarta = db.Column(db.String(80), unique=True, nullable=False)


    trkas = db.relationship("TrkaModel", back_populates="manifestacija", lazy="dynamic")
    #trkacs = db.relationship("TrkacModel", back_populates="manifestacija", lazy="dynamic")