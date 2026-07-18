from marshmallow import fields, validate, Schema
from app.core.constants import DataPlatform, SensitivityLevel

PLATFORM_VALUES = [platform.value for platform in DataPlatform]
SENSITIVITY_VALUES = [level.value for level in SensitivityLevel]


class DataProductCreateSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2, max=150))
    description = fields.Str(required=True, validate=validate.Length(min=2, max=2000))
    platform = fields.Str(
        required=True, validate=validate.OneOf(PLATFORM_VALUES)
    )  # It checks that the value supplied by the user is one of the allowed values.
    sensitivity_level = fields.Str(
        required=True, validate=validate.OneOf(SENSITIVITY_VALUES)
    )
    owner_user_id = fields.Int(required=True, validate=validate.Range(min=1))
    target_role_or_group = fields.Str(
        required=True, validate=validate.Length(min=2, max=255)
    )


class DataProductUpdateSchema(Schema):
    name = fields.Str(validate=validate.Length(min=2, max=150))
    description = fields.Str(validate=validate.Length(min=2, max=2000))
    platform = fields.Str(validate=validate.OneOf(PLATFORM_VALUES))
    sensitivity_level = fields.Str(validate=validate.OneOf(SENSITIVITY_VALUES))
    owner_user_id = fields.Int(validate=validate.Range(min=1))
    target_role_or_group = fields.Str(validate=validate.Length(min=2, max=255))
    is_active = fields.Bool()


class DataProductResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    organization_id = fields.Int(dump_only=True)
    name = fields.Str(dump_only=True)
    description = fields.Str(dump_only=True)
    platform = fields.Str(dump_only=True)
    sensitivity_level = fields.Str(dump_only=True)
    owner_user_id = fields.Int(dump_only=True)
    target_role_or_group = fields.Str(dump_only=True)
    is_active = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
