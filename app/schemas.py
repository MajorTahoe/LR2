from pydantic import BaseModel, Field, HttpUrl

class LinkCreate(BaseModel):
    url: HttpUrl
    description: str = Field(min_length=1, max_length=200)
    tags: list[str] = Field(default_factory=list)