from marshmallow import Schema, validate, fields


class PlainOrganizationSchema(Schema):  # organization input/output fields.
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    slug = fields.Str(required=True, validate=validate.Length(min=2, max=100))


class PlainUserSchema(Schema):  # safe user fields without password.
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    email = fields.Email(required=True)
    role = fields.Str(dump_only=True)


class RegisterUserSchema(
    PlainUserSchema
):  # inherits user fields and adds input-only password.
    password = fields.Str(
        required=True, load_only=True, validate=validate.Length(min=8)
    )


class RegisterSchema(Schema):  # validates the complete registration request.
    organization = fields.Nested(PlainOrganizationSchema(), required=True)
    user = fields.Nested(RegisterUserSchema(), required=True)


class RegisterResponseSchema(Schema):  # formats the successful response.
    message = fields.Str(dump_only=True)
    user = fields.Nested(PlainUserSchema(), dump_only=True)
    organization = fields.Nested(PlainOrganizationSchema(), dump_only=True)
