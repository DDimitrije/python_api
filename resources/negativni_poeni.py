from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import Negativni_poeniModel, ManifestacijaModel, TrkaModel
from schemas import Negativni_poeniSchema, Negativni_poeniUpdateSchema


blp = Blueprint("Negativni_poenis", "negativni_poenis", description="Operations on negativni_poenis")




@blp.route("/negativni_poeni/<int:trka_id>/negativni_poeni")
#class TrkacsInManifestacija(MethodView):
class Negativni_poenis(MethodView):
    @blp.response(200, Negativni_poeniSchema(many=True))
    def get(self, trka_id):
        trka = TrkaModel.query.get_or_404(trka_id)
        #print(trka.Negativni_poenis)

        return trka.Negativni_poenis.all()


@blp.route("/negativni_poeni")
class Negativni_poenisPost(MethodView):
    @blp.arguments(Negativni_poeniSchema)
    @blp.response(201, Negativni_poeniSchema)
    #def post(self, trkac_data, trka_id):
    def post(self, negativni_poeni_data):
        if Negativni_poeniModel.query.filter(
                #TrkacModel.trka_id == trka_id,
                Negativni_poeniModel.pozicija_negativni == negativni_poeni_data["pozicija_negativni"]
                #TrkacModel.tagCode == trkac_data["tagCode"],
                #TrkacModel.tagCode == trkac_data["tagCode"],
                #TrkacModel.imePrezime == trkac_data["imePrezime"],
                #TrkacModel.godinaRodjenja == trkac_data["godinaRodjenja"],
                #TrkacModel.mestoStanovanja == trkac_data["mestoStanovanja"],
                #TrkacModel.drzava == trkac_data["drzava"],
                #TrkacModel.klub == trkac_data["klub"],
                #TrkacModel.starosnaKategorija == trkac_data["starosnaKategorija"],
                #TrkacModel.email == trkac_data["email"],
                #TrkacModel.smsBroj == trkac_data["smsBroj"],
                #TrkacModel.storno == trkac_data["storno"],
                #TrkacModel.smsBroj == trkac_data["smsBroj"]
                ).first():
            abort(400, message="A Negativni_poeni with that name already exists in that trka.")

        negativni_poeni = Negativni_poeniModel(**negativni_poeni_data)

        try:
            db.session.add(negativni_poeni)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(
                500,
                message=str(e),
            )

        return negativni_poeni

    @blp.response(200, Negativni_poeniSchema(many=True))
    def get(self):
        return Negativni_poeniModel.query.all()


@blp.route("/trka/<int:trka_id>/negativni_poeni/<int:negativni_poeni_id>")
class LinkTagsToItem(MethodView):
    @blp.response(201, Negativni_poeniSchema)
    def post(self, trka_id, negativni_poeni_id):
        trka = TrkaModel.query.get_or_404(trka_id)
        negativni_poeni = Negativni_poeniModel.query.get_or_404(negativni_poeni_id)

        trka.negativni_poenis.append(negativni_poeni)

        try:
            db.session.add(trka)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the tag.")

        return negativni_poeni


@blp.route("/negativni_poeni/<int:negativni_poeni_id>")
class Negativni_poenis(MethodView):
    @blp.response(200, Negativni_poeniSchema)
    def get(self, negativni_poeni_id):
        negativni_poeni = Negativni_poeniModel.query.get_or_404(negativni_poeni_id)
        return negativni_poeni

    @blp.arguments(Negativni_poeniUpdateSchema)
    @blp.response(200, Negativni_poeniSchema)
    def put(self, negativni_poeni_data, negativni_poeni_id):
        negativni_poeni = Negativni_poeniModel.query.get(negativni_poeni_id)
        print( negativni_poeni )
        print( negativni_poeni_id)

        if negativni_poeni:
            negativni_poeni.negativni_poeni = negativni_poeni_data["negativni_poeni"]
            negativni_poeni.pozicija_negativni = negativni_poeni_data["pozicija_negativni"]
            negativni_poeni.broj_poena_negativni = negativni_poeni_data["broj_poena_negativni"]
            negativni_poeni.kazna_sec_negativni = negativni_poeni_data["kazna_sec_negativni"]
            negativni_poeni.storno_negativni = negativni_poeni_data["storno_negativni"]
            negativni_poeni.trka_id = negativni_poeni_data["trka_id"]

        else:
            negativni_poeni = Negativni_poeniModel(id_negativni_poeni=negativni_poeni_id, **negativni_poeni_data)
        db.session.add(negativni_poeni)
        db.session.commit()

        return negativni_poeni

    @blp.response(
        202,
        description="Deletes a negativni_poeni if no android is tagged with it.",
        example={"message": "Negativni_poeni deleted."},
    )
    @blp.alt_response(404, description="Negativni_poeni not found.")
    @blp.alt_response(
        400,
        description="Negativni_poeni is not deleted.",
    )
    def delete(self, negativni_poeni_id):
        negativni_poeni = Negativni_poeniModel.query.get_or_404(negativni_poeni_id)
        db.session.delete(negativni_poeni)
        db.session.commit()
        return {"message": "Negativni_poeni deleted."}, 200


@blp.route("/negativni_poeni/<int:pozicija_negativni>/")
class Pozicija_negativniList(MethodView):
    @blp.response(200, Negativni_poeniSchema(many=True))
    def get(self,  pozicija_negativni):
        #print("type " , type(bib_android))
        pozicija_negativni_all = Negativni_poeniModel.query.all()
        for aaaa in pozicija_negativni_all:
            if aaaa.pozicija_negativni == pozicija_negativni:
                dic = {aaaa}
                return dic
        return abort(400, message=f"trazen broj nije pronađen {pozicija_negativni} .")