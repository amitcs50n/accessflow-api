from marshmallow import Schema, fields, validate
from app.core.constants import AccessLevel

ACCESS_LEVEL_VALUES = [level.value for level in AccessLevel]


class AccessRequestCreateSchema(Schema):
    data_product_id = fields.Int(
        required=True,
        validate=validate.Range(min=1),
    )
    access_level = fields.Str(
        required=True,
        validate=validate.OneOf(ACCESS_LEVEL_VALUES),
    )
    business_justification = fields.Str(
        required=True,
        validate=validate.Length(min=10, max=2000),
    )
    expiration_date = fields.Date(required=True)


class AccessRequestResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    organization_id = fields.Int(dump_only=True)
    requester_id = fields.Int(dump_only=True)
    data_product_id = fields.Int(dump_only=True)
    access_level = fields.Str(dump_only=True)
    business_justification = fields.Str(dump_only=True)
    expiration_date = fields.Date(dump_only=True)
    status = fields.Str(dump_only=True)
    source_system = fields.Str(dump_only=True)
    servicenow_request_number = fields.Str(
        dump_only=True,
        allow_none=True,
    )
    servicenow_sys_id = fields.Str(
        dump_only=True,
        allow_none=True,
    )
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
