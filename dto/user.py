from pydantic import BaseModel, conint
from typing import Optional

class User(BaseModel):
    name : str
    age : Optional[conint(gt=18)] = None