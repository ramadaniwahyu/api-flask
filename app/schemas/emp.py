from marshmallow import Schema, fields

class InitialEmpSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str()
    nip = fields.Str()
    jabatan = fields.Str()
    
class EmpSchema(InitialEmpSchema):
    relaas = fields.List(fields.Nested('RelaasSchema'), dump_only=True)