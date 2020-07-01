import enum

from ib_common.constants import BaseEnumClass


class CodeLanguage(BaseEnumClass, enum.Enum):
    python = "PYTHON"
    c_language = "C"
    c_plus_plus = "CPP"
    python36 = "PYTHON36"
    python37 = "PYTHON37"
    python38 = "PYTHON38"
    python38_datascience = "PYTHON38_DATASCIENCE"
    python38_aiml = "PYTHON38_AIML"

class Project_Type(BaseEnumClass, enum.Enum):
    Classic_Software = "Classic Software"
    Financial = "Financial"
    CRM = "CRM"
    
class IssueType(BaseEnumClass, enum.Enum):
    Task ="Task"
    Bug ="Bug"
    Developer_story = "Developer Story"
    User_story = "User Story"
    Enhancement = "Enhancement"
