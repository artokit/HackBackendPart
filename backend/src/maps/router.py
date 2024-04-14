from fastapi import APIRouter
from maps.schemas import Coordinate, Coordinates, AllDots
from maps import service

router = APIRouter(prefix="/api/maps", tags=["Maps"])


@router.get("/", response_model=Coordinates)
async def get_coordinates(start: str, end: str):
    return Coordinates(coordinates=await service.get_coordinates(start, end))


@router.post("/add_dot")
async def add_dot(coordinate: Coordinate):
    await service.add_dot(coordinate)


@router.put("/add_line")
async def add_line(dot_name1: str, dot_name2: str):
    await service.add_line(dot_name1, dot_name2)


@router.get("/get_all_destinations")
async def get_all_destinations():
    return await service.get_all_destinations_name()


@router.get("/get_dots", response_model=AllDots)
async def get_all_dots():
    return await service.get_all_dots()
