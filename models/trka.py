from db import db


#class ItemModel(db.Model):
#    __tablename__ = "items"

class TrkaModel(db.Model):
    __tablename__ = "trkas"


    id_trka = db.Column(db.Integer, primary_key=True)
    nazivTrka = db.Column(db.String(80), unique=False, nullable=False)
    startTrka = db.Column(db.String(80), unique=False, nullable=False)
    krajTrka = db.Column(db.String(80), unique=False, nullable=False)
    storno = db.Column(db.String(80), unique=False, nullable=False)



    manifestacija_id = db.Column(
        db.Integer, db.ForeignKey("manifestacijas.id_manifestacija"), unique=False, nullable=False
    ) # mora zbog povezivanja sa manifestacijom
    manifestacija = db.relationship("ManifestacijaModel", back_populates="trkas") #items = trkas


    #trkas = db.relationship("TrkaModel", back_populates="manifestacija", lazy="dynamic")
    trkacs = db.relationship("TrkacModel", back_populates="trka",  lazy="dynamic")#, lazy="dynamic") #, secondary="trkas_trkacs")

    androids = db.relationship("AndroidModel", back_populates="trka",  lazy="dynamic")
    citacs = db.relationship("CitacModel", back_populates="trka",  lazy="dynamic")
    negativni_poenis = db.relationship("Negativni_poeniModel", back_populates="trka",  lazy="dynamic")
