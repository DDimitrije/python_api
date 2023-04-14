from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TrkacModel, ManifestacijaModel, TrkaModel
from schemas import TrkacSchema, TrkacUpdateSchema


blp = Blueprint("Trkacs", "trkacs", description="Operations on trkacs")


@blp.route("/trka/<string:trka_id>/trkac")
#class TrkacsInManifestacija(MethodView):
class Trkacs(MethodView):
    @blp.response(200, TrkacSchema(many=True))
    def get(self, trka_id):
        trka = TrkaModel.query.get_or_404(trka_id)
        print(trka.trkacs)

        return trka.trkacs.all()  # lazy="dynamic" means 'tags' is a query

@blp.route("/trkac")
class TrkacsPost(MethodView):
    @blp.arguments(TrkacSchema)
    @blp.response(201, TrkacSchema)
    #def post(self, trkac_data, trka_id):
    def post(self, trkac_data):
        if TrkacModel.query.filter(
                #TrkacModel.trka_id == trka_id,
                TrkacModel.bib == trkac_data["bib"],
                TrkacModel.tagCode == trkac_data["tagCode"]
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
            abort(400, message="A trkac with that name already exists in that trka.")

        trkac = TrkacModel(**trkac_data)

        try:
            db.session.add(trkac)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(
                500,
                message=str(e),
            )

        return trkac

@blp.route("/trka/<string:trka_id>/trkac/<string:trkac_id>")
class LinkTagsToItem(MethodView):
    @blp.response(201, TrkacSchema)
    def post(self, trka_id, trkac_id):
        trka = TrkaModel.query.get_or_404(trka_id)
        trkac = TrkacModel.query.get_or_404(trkac_id)

        trka.trkacs.append(trkac)

        try:
            db.session.add(trka)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the tag.")

        return trkac


@blp.route("/trkac/<string:trkac_id>")
class Trkac(MethodView):
    @blp.response(200, TrkacSchema)
    def get(self, trkac_id):
        trkac = TrkacModel.query.get_or_404(trkac_id)
        return trkac

    @blp.arguments(TrkacUpdateSchema)
    @blp.response(200, TrkacSchema)
    def put(self, trkac_data, trkac_id):
        trkac = TrkacModel.query.get(trkac_id)
        print( trkac )
        print( trkac_id)

        if trkac:
            trkac.bib = trkac_data["bib"]
            trkac.tagCode = trkac_data["tagCode"]
            trkac.imePrezime = trkac_data["imePrezime"]
            trkac.godinaRodjenja = trkac_data["godinaRodjenja"]
            trkac.mestoStanovanja = trkac_data["mestoStanovanja"]
            trkac.drzava = trkac_data["drzava"]
            trkac.klub = trkac_data["klub"]
            trkac.starosnaKategorija = trkac_data["starosnaKategorija"]
            trkac.email = trkac_data["email"]
            trkac.smsBroj = trkac_data["smsBroj"]
            trkac.storno = trkac_data["storno"]
            trkac.trka_id = trkac_data["trka_id"]

        else:
            trkac = TrkacModel(id_trkac=trkac_id, **trkac_data)
        db.session.add(trkac)
        db.session.commit()

        return trkac

    @blp.response(
        202,
        description="Deletes a trkac if no item is tagged with it.",
        example={"message": "Trkac deleted."},
    )
    @blp.alt_response(404, description="Trkac not found.")
    @blp.alt_response(
        400,
        description="Trkac is not deleted.",
    )
    def delete(self, trkac_id):
        trkac = TrkacModel.query.get_or_404(trkac_id)
        db.session.delete(trkac)
        db.session.commit()
        return {"message": "Trkac deleted."}, 200

@blp.route("/trkac/<string:bib>/")
class TrkacList(MethodView):
    @blp.response(200, TrkacSchema(many=True))
    def get(self,  bib):
        #print("type " , type(bib_android))
        trkac_all = TrkacModel.query.all()
        for aaaa in trkac_all:
            if aaaa.bib == bib:
                dic = {aaaa}
                return dic
        return abort(400, message=f"trazen broj nije pronađen {bib} .")