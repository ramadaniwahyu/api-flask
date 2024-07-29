from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from app import db
from app.models import RelaasModel
from app.schemas import RelaasSchema


blp = Blueprint("Relaas", "relaas", description="Operations on relaas")


@blp.route("/relaas/<string:relaas_id>")
class Relaas(MethodView):
    @blp.response(200, RelaasSchema)
    def get(self, relaas_id):
        relaas = RelaasModel.query.get_or_404(relaas_id)
        return relaas

    def delete(self, relaas_id):
        relaas = RelaasModel.query.get_or_404(relaas_id)
        db.session.delete(relaas)
        db.session.commit()
        return {"message": "Relaas deleted"}, 200
    
    @blp.arguments(RelaasSchema)
    @blp.response(200, RelaasSchema)
    def put(self, relaas_data, relaas_id):
        relaas = RelaasModel.query.get(relaas_id)

        if relaas:
            relaas.address = relaas_data["address"]
            relaas.name = relaas_data["name"]
            relaas.about = relaas_data["about"]
            relaas.posted_on = relaas_data["posted_on"]
            relaas.case_no = relaas_data["case_no"]
            relaas.country = relaas_data["country"]
            relaas.province = relaas_data["province"]
            relaas.city = relaas_data["city"]
            relaas.district = relaas_data["district"]
            relaas.sub_district = relaas_data["sub_district"]
            relaas.package_id = relaas_data["package_id"]
            relaas.package_result = relaas_data["package_result"]
        else:
            relaas = RelaasModel(id=relaas_id, **relaas_data)

        # db.session.add(school)
        db.session.commit()

        return relaas


@blp.route("/relaas")
class RelaasList(MethodView):
    @blp.response(200, RelaasSchema(many=True))
    def get(self):
        return RelaasModel.query.all()

    @blp.arguments(RelaasSchema)
    @blp.response(201, RelaasSchema)
    def post(self, relaas_data):
        relaas = RelaasModel(**relaas_data)
        try:
            db.session.add(relaas)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A school with that id already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the relaas.")

        return relaas
