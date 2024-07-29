from app import db

class RelaasModel(db.Model):
    __tablename__ = "relaas"

    id = db.Column(db.Integer, primary_key=True)
    about = db.Column(db.String(300))
    posted_on = db.Column(db.DateTime)
    case_no = db.Column(db.String(200))
    name = db.Column(db.String(80))
    address = db.Column(db.Text())
    country = db.Column(db.String(100))
    province = db.Column(db.String(100))
    city = db.Column(db.String(100))
    district = db.Column(db.String(100))
    sub_district = db.Column(db.String(100))
    package_id = db.Column(db.String(100))
    package_result = db.Column(db.String(100))
    
    emp_id = db.Column(
        db.Integer, db.ForeignKey("emps.id")
        )
    emps = db.relationship("EmpModel", back_populates="relaas")