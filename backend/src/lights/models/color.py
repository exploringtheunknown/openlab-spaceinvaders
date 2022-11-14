from pydantic import BaseModel
from typing import Tuple


class Color(BaseModel):
    r: int
    g: int
    b: int

    def values(self) -> Tuple[int, int, int]:
        return (self.r, self.g, self.b)
