from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import CitacModel, ManifestacijaModel, TrkaModel
from schemas import CitacSchema, CitacUpdateSchema


blp = Blueprint("Citacs", "citacs", description="Operations on citacs")



@blp.route("/citac/<int:trka_id>/citac")
#class TrkacsInManifestacija(MethodView):
class Citacs(MethodView):
    @blp.response(200, CitacSchema(many=True))
    def get(self, trka_id):
        trka = TrkaModel.query.get_or_404(trka_id)
        print(trka.citacs)

        return trka.citacs.all()  # lazy="dynamic" means 'tags' is a query

@blp.route("/citac")
class CitacsPost(MethodView):
    @blp.arguments(CitacSchema)
    @blp.response(201, CitacSchema)
    #def post(self, trkac_data, trka_id):
    def post(self, citac_data):
        if CitacModel.query.filter(
                #TrkacModel.trka_id == trka_id,
                CitacModel.bib_citac == citac_data["bib_citac"]
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
            abort(400, message="A citac with that name already exists in that trka.")

        citac = CitacModel(**citac_data)

        try:
            db.session.add(citac)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(
                500,
                message=str(e),
            )

        return citac


@blp.response(200, CitacSchema)
class CitacList(MethodView):
    @blp.response(200, CitacSchema(many=True))
    def get(self):
        return CitacModel.query.all()

@blp.route("/trka/<int:trka_id>/android/<int:android_id>")
class LinkTagsToItem(MethodView):
    @blp.response(201, CitacSchema)
    def post(self, trka_id, citac_id):
        trka = TrkaModel.query.get_or_404(trka_id)
        citac = CitacModel.query.get_or_404(citac_id)

        trka.citacs.append(citac)

        try:
            db.session.add(trka)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the tag.")

        return citac


@blp.route("/citac/<int:citac_id>")
class Android(MethodView):
    @blp.response(200, CitacSchema)
    def get(self, citac_id):
        citac = CitacModel.query.get_or_404(citac_id)
        return citac

    @blp.arguments(CitacUpdateSchema)
    @blp.response(200, CitacSchema)
    def put(self, citac_data, citac_id):
        citac = CitacModel.query.get(citac_id)
        print( citac )
        print( citac_id)

        if citac:
            citac.bib_citac = citac_data["bib_citac"]
            citac.ime_preziem_citac = citac_data["ime_preziem_citac"]
            citac.age_group_citac = citac_data["age_group_citac"]
            citac.age_gun_time = citac_data["age_gun_time"]
            citac.age_net_time = citac_data["age_net_time"]
            citac.age_storno = citac_data["age_storno "]
            citac.trka_id = citac_data["trka_id"]

        else:
            citac = CitacModel(id_citac=citac_id, **citac_data)
        db.session.add(citac)
        db.session.commit()

        return citac

    @blp.response(
        202,
        description="Deletes a android if no android is tagged with it.",
        example={"message": "Citac deleted."},
    )
    @blp.alt_response(404, description="Citac not found.")
    @blp.alt_response(
        400,
        description="Citac is not deleted.",
    )
    def delete(self, citac_id):
        citac = CitacModel.query.get_or_404(citac_id)
        db.session.delete(citac)
        db.session.commit()
        return {"message": "Citac deleted."}, 200


@blp.route("/citac/<int:bib_citac>/")
class CitacList(MethodView):
    @blp.response(200, CitacSchema(many=True))
    def get(self,  bib_citac):
        #print("type " , type(bib_android))
        citac_all = CitacModel.query.all()
        for aaaa in citac_all:
            if aaaa.bib_citac == bib_citac:
                dic = {aaaa}
                return dic
        return abort(400, message=f"trazen broj nije pronađen {bib_citac} .")
