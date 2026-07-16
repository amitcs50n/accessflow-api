from enum import Enum


# An Enum (Enumeration) is a way to define a fixed set of named constant values.
class UserRole(str, Enum):
    REQUESTER = "REQUESTER"
    MANAGER = "MANAGER"
    DATA_OWNER = "DATA_OWNER"
    PLATFORM_ADMIN = "PLATFORM_ADMIN"
    AUDITOR = "AUDITOR"
