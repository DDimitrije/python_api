from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import AndroidModel, ManifestacijaModel, TrkaModel
from schemas import AndroidSchema, AndroidUpdateSchema


blp = Blueprint("Androids", "androids", description="Operations on androids")


@blp.route("/trka/<int:trka_id>/android")
#class TrkacsInManifestacija(MethodView):
class Androids(MethodView):
    @blp.response(200, AndroidSchema(many=True))
    def get(self, trka_id):
        trka = TrkaModel.query.get_or_404(trka_id)
        print(trka.androids)

        return trka.androids.all()


@blp.route("/android")
class AndroidsPost(MethodView):
    @blp.arguments(AndroidSchema)
    @blp.response(201, AndroidSchema)
    #def post(self, trkac_data, trka_id):
    def post(self, android_data):
        if AndroidModel.query.filter(
                #TrkacModel.trka_id == trka_id,
                AndroidModel.bib_android == android_data["bib_android"]
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
            abort(400, message="A trkac with that name already exists in that trka.")

        android = AndroidModel(**android_data)

        try:
            db.session.add(android)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(
                500,
                message=str(e),
            )

        return android

@blp.route("/trka/<int:trka_id>/android/<int:android_id>")
class LinkTagsToItem(MethodView):
    @blp.response(201, AndroidSchema)
    def post(self, trka_id, android_id):
        trka = TrkaModel.query.get_or_404(trka_id)
        android = AndroidModel.query.get_or_404(android_id)

        trka.trkacs.append(android)

        try:
            db.session.add(trka)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the tag.")

        return android


@blp.route("/android/int:android_id>")
class Android(MethodView):
    @blp.response(200, AndroidSchema)
    def get(self, android_id):
        android = AndroidModel.query.get_or_404(android_id)
        return android

    @blp.arguments(AndroidUpdateSchema)
    @blp.response(200, AndroidSchema)
    def put(self, android_data, android_id):
        android = AndroidModel.query.get(android_id)
        print( android )
        print( android_id)

        if android:
            android.bib_android = android_data["bib_android"]
            android.pozicija_android = android_data["pozicija_android"]
            android.tag_code_android = android_data["tag_code_android"]
            android.vreme_sistemsko_android = android_data["vreme_sistemsko_android"]
            android.storno_android = android_data["storno_android"]
            android.trka_id = android_data["trka_id"]
        else:
            android = AndroidModel(id_android=android_id, **android_data)
        db.session.add(android)
        db.session.commit()

        return android

    @blp.response(
        202,
        description="Deletes a android if no android is tagged with it.",
        example={"message": "Android deleted."},
    )
    @blp.alt_response(404, description="Android not found.")
    @blp.alt_response(
        400,
        description="Android is not deleted.",
    )
    def delete(self, android_id):
        android = AndroidModel.query.get_or_404(android_id)
        db.session.delete(android)
        db.session.commit()
        return {"message": "Android deleted."}, 200

@blp.route("/android")
class AndroidList(MethodView):
    @blp.response(200, AndroidSchema(many=True))
    def get(self):
        return AndroidModel.query.all()

@blp.route("/android/<string:bib_android>/")
class AndroidList(MethodView):
    @blp.response(200, AndroidSchema(many=True))
    def get(self,  bib_android):
        #print("type " , type(bib_android))
        android_all = AndroidModel.query.all()
        for aaaa in android_all:
            if aaaa.bib_android == bib_android:
                dic = {aaaa}
                return dic
        return abort(400, message=f"trazen broj nije pronađen {bib_android} .")


