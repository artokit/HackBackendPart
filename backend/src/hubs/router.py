from fastapi import APIRouter
from hubs.schemas import SuccessAddCompany, AddTask, SuccessAddTask, GetAllTasksByCompany, AllCompaniesResponse
from hubs import service


router = APIRouter(prefix="/api/hub", tags=['Tasks'])


@router.post("/add_company", response_model=SuccessAddCompany)
async def add_company(company_name: str):
    return await service.add_company(company_name)


@router.post("/", response_model=SuccessAddTask)
async def add_task(task: AddTask):
    return await service.add_task(task)


@router.get("/", response_model=GetAllTasksByCompany)
async def get_tasks():
    return await service.get_all_tasks_by_company()


@router.get("/get_companies", response_model=AllCompaniesResponse)
async def get_companies():
    return await service.get_companies()
