from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import TrkaModel
from schemas import TrkaSchema, TrkaUpdateSchema

blp = Blueprint("Trkas", "trkas", description="Operations on trkas")


@blp.route("/trka/<string:trka_id>")
class Trka(MethodView):
    @blp.response(200, TrkaSchema)
    def get(self, trka_id):
        trka = TrkaModel.query.get_or_404(trka_id)
        return trka

    def delete(self, trka_id):
        trka = TrkaModel.query.get_or_404(trka_id)
        db.session.delete(trka)
        db.session.commit()
        return {"message": "Trka deleted."}

    @blp.arguments(TrkaUpdateSchema)
    @blp.response(200, TrkaSchema)
    def put(self, trka_data, trka_id):
        trka = TrkaModel.query.get(trka_id)
        print(trka_data["nazivTrka"])
        print(trka_data["startTrka"])
        print(trka_data["krajTrka"])
        print(trka_data["storno"])
        #print(item_data["net_time"])

        if trka:
            trka.nazivTrka = trka_data["nazivTrka"]
            trka.startTrka = trka_data["startTrka"]
            trka.krajTrka = trka_data["krajTrka"]
            trka.storno = trka_data["storno"]
            trka.manifestacija_id = trka_data["manifestacija_id"]
            #trka.net_time = trka_data["net_time"]
        else:
            trka = TrkaModel(id_trka=trka_id, **trka_data)

        db.session.add(trka)
        db.session.commit()

        return trka


@blp.route("/trka")
class TrkaList(MethodView):
    @blp.response(200, TrkaSchema(many=True))
    def get(self):
        return TrkaModel.query.all()

    @blp.arguments(TrkaSchema)
    @blp.response(201, TrkaSchema)
    def post(self, trka_data):
        trka = TrkaModel(**trka_data)

        try:
            db.session.add(trka) #dodavanje novog u bazu
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the trka. ")

        return trka