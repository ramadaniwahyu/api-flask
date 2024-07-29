from marshmallow import Schema, fields

class InitialRelaasSchema(Schema):
    id = fields.Str(dump_only=True)
    about = fields.Str()
    posted_on = fields.DateTime()
    case_no = fields.Str()
    name = fields.Str()
    address = fields.Str()
    country = fields.Str()
    province = fields.Str()
    city = fields.Str()
    district = fields.Str()
    sub_district = fields.Str()
    emp_id = fields.Int()
    
class RelaasSchema(InitialRelaasSchema):
    package_id = fields.Str()
    package_result = fields.Str()