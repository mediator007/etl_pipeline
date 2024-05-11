from enum import StrEnum
from typing import Optional
from pydantic import BaseModel


class Types(StrEnum):
    INSTITUTE: str = "Institute"
    COLLEGE: str = "College"
    UNIVERSITY: str = "University"


class University(BaseModel):
    name: str
    country: str
    type: Optional[Types] = None
