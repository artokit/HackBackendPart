from pydantic import BaseModel


class AddCompany(BaseModel):
    name: str


class SuccessAddCompany(BaseModel):
    id: int
    name: str


class AddTask(BaseModel):
    company_id: int
    title: str
    description: str
    subjects: list[str]
    level: str


class SuccessAddTask(BaseModel):
    id: int
    company: str
    title: str
    description: str
    subjects: list[str]
    level: str


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    subjects: list[str]
    level: str


class AllCompaniesResponse(BaseModel):
    res: list[SuccessAddCompany]


class CompanyTask(BaseModel):
    id: int
    company_name: str
    tasks: list[TaskResponse]


class GetAllTasksByCompany(BaseModel):
    res: list[CompanyTask]
