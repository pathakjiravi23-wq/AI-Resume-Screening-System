from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Personal_details(BaseModel):
    name: str | None = None
    phone_number: str | None = None
    email: EmailStr | None = None
    linkdin: str | None = None
    github: str | None = None
    portfolio: str | None = None
    other_profiles: str | None = None


class Edu_details(BaseModel):
    institution: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    location: str | None = None
    field_of_study: str | None = None
    grade: str | None = None
    degree: str | None = None


class Expe_details(BaseModel):
    company: str | None = None
    role: str | None = None
    location: str | None = None
    employement_type: str | None = None
    responsibilities: list[str] = Field(default_factory=list)
    start_date: str | None = None
    end_date: str | None = None


class Project(BaseModel):
    name: str
    description: Optional[str] = None
    technologies: list[str] = Field(default_factory=list)
    responsibilities: list[str] = Field(default_factory=list)
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    github_url: Optional[str] = None
    live_url: Optional[str] = None


class Skills_details(BaseModel):
    programming_languages: list[str] = Field(default_factory=list)
    frameworks: list[str] = Field(default_factory=list)
    libraries: list[str] = Field(default_factory=list)
    databases: list[str] = Field(default_factory=list)
    tools: list[str] = Field(default_factory=list)
    cloud: list[str] = Field(default_factory=list)
    other: list[str] = Field(default_factory=list)


class Achievement(BaseModel):
    title: str
    description: Optional[str] = None
    organization: Optional[str] = None
    date: Optional[str] = None
    rank: Optional[str] = None
    url: Optional[str] = None


class Certification(BaseModel):
    name: str
    issuer: Optional[str] = None
    issue_date: Optional[str] = None
    expiry_date: Optional[str] = None
    credential_id: Optional[str] = None
    credential_url: Optional[str] = None


class Publication(BaseModel):
    title: str
    publisher: Optional[str] = None
    publication_date: Optional[str] = None
    url: Optional[str] = None
    authors: list[str] = Field(default_factory=list)


class Language(BaseModel):
    language_name: str | None = None
    proficiency: Optional[str] = None


class Resume(BaseModel):
    personal_info: Personal_details
    summary: Optional[str] = None

    education: list[Edu_details] = Field(default_factory=list)
    experience: list[Expe_details] = Field(default_factory=list)
    projects: list[Project] = Field(default_factory=list)

    skills: Skills_details

    achievements: list[Achievement] = Field(default_factory=list)
    certifications: list[Certification] = Field(default_factory=list)
    publications: list[Publication] = Field(default_factory=list)
    languages: list[Language] = Field(default_factory=list)
