from marshmallow import Schema, validate,fields

# class RegisterSchema(Schema):
#     organization_name = fields.String(required=True, validate=validate.Length(min=2, max=100))
#     organization_slug = fields.String(required=True, validate=validate.Length(min=2, max=100))
#     name = fields.String(required=True,validate=validate.Length(min=2, max=100))
#     email = fields.Email(required=True)
#     password = fields.String(required=True, load_only=True, validate=validate.Length(min=8))
#
#
# class UserResponseSchema(Schema):
#     id = fields.Integer(dump_only=True)
#     name = fields.String(dump_only=True)
#     email = fields.Email(dump_only=True)
#     role = fields.String(dump_only=True)
#     organization_id = fields.Integer(dump_only=True)
#
# class RegisterResponseSchema(Schema):
#     message = fields.String(dump_only=True)
#     user = fields.Nested(UserResponseSchema, dump_only=True)
#
#




class PlainOrganizationSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    slug = fields.Str(required=True, validate=validate.Length(min=2, max=100))


class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    email = fields.Email(required=True)
    role = fields.Str(dump_only=True)


class RegisterUserSchema(PlainUserSchema):
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=8))


class RegisterSchema(Schema):
    organization = fields.Nested(PlainOrganizationSchema(), required=True)
    user = fields.Nested(RegisterUserSchema(), required=True)


class RegisterResponseSchema(Schema):
    message = fields.Str(dump_only=True)
    user = fields.Nested(PlainUserSchema(), dump_only=True)
    organization = fields.Nested(PlainOrganizationSchema(), dump_only=True)