from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import ManifestacijaModel
from schemas import ManifestacijaSchema


blp = Blueprint("Manifestacijas", "manifestacijas", description="Operations on manifestacijas")


@blp.route("/manifestacija/<int:manifestacija_id>")
class Manifestacija(MethodView):
    @blp.response(200, ManifestacijaSchema)
    def get(self, manifestacija_id):
        manifestacija = ManifestacijaModel.query.get_or_404(manifestacija_id)
        return manifestacija

    def delete(self, manifestacija_id):
        manifestacija = ManifestacijaModel.query.get_or_404(manifestacija_id)
        db.session.delete(manifestacija)
        db.session.commit()
        return {"message": "manifestacija deleted"}, 200


@blp.route("/manifestacija")
class ManifestacijaList(MethodView):
    @blp.response(200, ManifestacijaSchema(many=True))
    def get(self):
        return ManifestacijaModel.query.all()

    @blp.arguments(ManifestacijaSchema)
    @blp.response(201, ManifestacijaSchema)
    def post(self, manifestacija_data):
        manifestacija = ManifestacijaModel(**manifestacija_data)
        try:
            db.session.add(manifestacija)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A manifestacija with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message=" Store An error occurred creating the manifestacija.")

        return manifestacija
