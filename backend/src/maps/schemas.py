from typing import Optional
from pydantic import BaseModel


class Coordinate(BaseModel):
    name: Optional[str] = None
    x: int
    y: int


class Coordinates(BaseModel):
    coordinates: list[int]


class GetCoordinates(BaseModel):
    start: str
    end: str


class GraphDot(BaseModel):
    name: str
    x: int
    y: int
    nexts: list[str]


class AllDots(BaseModel):
    graph: list[GraphDot]
