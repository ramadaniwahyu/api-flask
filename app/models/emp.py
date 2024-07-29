from app import db

class EmpModel(db.Model):
    __tablename__ = "emps"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    nip = db.Column(db.String(20), unique=True)
    jabatan = db.Column(db.String(100))

    relaas = db.relationship("RelaasModel", back_populates="emps", lazy="dynamic")