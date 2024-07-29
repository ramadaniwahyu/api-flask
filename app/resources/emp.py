from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models import EmpModel
from app.schemas import EmpSchema

blp = Blueprint("Emps", "emps", description="Operations on emps")

@blp.route("/emp/<int:emp_id>")
class Emp(MethodView):
    # @jwt_required()
    @blp.response(200, EmpSchema)
    def get(self, emp_id):
        emp = EmpModel.query.get_or_404(emp_id)
        return emp

    # @jwt_required()
    def delete(self, emp_id):
        # jwt = get_jwt()
        # if not jwt.get("is_admin"):
        #     abort(401, message="Admin privilege required.")

        emp = EmpModel.query.get_or_404(emp_id)
        db.session.delete(emp)
        db.session.commit()
        return {"message": "Employee deleted."}

    @blp.arguments(EmpSchema)
    @blp.response(200, EmpSchema)
    def put(self, emp_data, emp_id):
        emp = EmpModel.query.get(emp_id)

        if emp:
            emp.name = emp_data["name"]
            emp.nip = emp_data["nip"]
            emp.jabatan = emp_data["jabatan"]
        else:
            emp = EmpModel(id=emp_id, **emp_data)

        db.session.add(emp)
        db.session.commit()

        return emp


@blp.route("/emp")
class EmpList(MethodView):
    # @jwt_required()
    @blp.response(200, EmpSchema(many=True))
    def get(self):
        return EmpModel.query.all()

    # @jwt_required(fresh=True)
    @blp.arguments(EmpSchema)
    @blp.response(201, EmpSchema)
    def post(self, emp_data):
        print(emp_data)
        emp = EmpModel(**emp_data)

        try:
            db.session.add(emp)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the Employee.")

        return emp
