from enum import Enum


class DbOwner(Enum):
    ENT = "ENTERPRISE"
    BU = "BUSINESS_UNIT"


class Database(Enum):
    DW = "DW"
    DSPROD = "DSPROD"
    SALESFORCE = "SALESFORCE"
    DYNAMODB = "DYNAMODB"
    FINANCE = "FINANCE"
    SALES = "SALES"
    CEAR = "CEAR"


class Env(Enum):
    DEV = "DEV"
    UAT = "UAT"
    PRD = "PROD"


class Layer(Enum):
    RL = "RL"
    INT = "INT"
    SHARE = "SHARE"
    PRES = "PRES"


class WarehousePrivileges(Enum):
    MODIFY = {
        "name": "modify",
        "value": ["USAGE", "OPERATE", "MODIFY", "MONITOR"],
        "description": "Privilege for administrators that need to setup warehouses",
    }
    MONITOR = {
        "name": "monitor",
        "value": ["MONITOR"],
        "description": "Privilege for service accounts that monitor warehouses",
    }
    OPERATE = {
        "name": "operate",
        "value": ["USAGE", "OPERATE", "MONITOR"],
        "description": "Privilege for functional roles that need to enable/disable warehouses",
    }
    USAGE = {
        "name": "usage",
        "value": ["USAGE", "MONITOR"],
        "description": "Privilege for most functional roles that use warehouses (i.e. analysts, engineers, etc.)",
    }


class DatabasePrivileges(Enum):
    READ = "R"
    READ_WRITE = "RW"


class Roles(Enum):
    AR = "Access Role"
    FR = "Functional Role"
