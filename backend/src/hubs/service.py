from typing import Optional
from hubs import repo
from hubs.models import Company
from hubs.schemas import AddTask, SuccessAddTask, GetAllTasksByCompany, CompanyTask, AllCompaniesResponse, \
    SuccessAddCompany


async def add_company(name: str) -> Optional[Company]:
    return await repo.add_company(name)


async def add_task(task: AddTask) -> SuccessAddTask:
    res = await repo.add_task(task)
    return SuccessAddTask(
        id=res.id,
        company=(await repo.get_company_by_id(res.company_id)).name,
        title=res.title,
        description=res.description,
        subjects=res.subjects.split(";"),
        level=res.level
    )


async def get_all_tasks_by_company() -> GetAllTasksByCompany:
    companies = await repo.get_all_task_companies()
    return GetAllTasksByCompany(
        res=[CompanyTask(
            id=i.id,
            company_name=i.name,
            tasks=await repo.get_task_by_company_id(i.id)
        ) for i in companies]
    )


async def get_companies() -> AllCompaniesResponse:
    return AllCompaniesResponse(
        res=[SuccessAddCompany(id=i.id, name=i.name) for i in await repo.get_all_companies()]
    )
