from enum import Enum


# An Enum (Enumeration) is a way to define a fixed set of named constant values.
class UserRole(str, Enum):
    REQUESTER = "REQUESTER"
    MANAGER = "MANAGER"
    DATA_OWNER = "DATA_OWNER"
    PLATFORM_ADMIN = "PLATFORM_ADMIN"
    AUDITOR = "AUDITOR"


class DataPlatform(str, Enum):
    SNOWFLAKE = "SNOWFLAKE"
    DATABRICKS = "DATABRICKS"
    POWER_BI = "POWER_BI"
    AZURE_AD = "AZURE_AD"
    INTERNAL_API = "INTERNAL_API"


class SensitivityLevel(str, Enum):
    PUBLIC = "PUBLIC"
    INTERNAL = "INTERNAL"
    CONFIDENTIAL = "CONFIDENTIAL"
    RESTRICTED = "RESTRICTED"
