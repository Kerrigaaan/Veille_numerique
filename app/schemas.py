from pydantic import BaseModel
from datetime import datetime

class ArticleBase(BaseModel):
    title: str
    summary: str
    url: str

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int
    published_at: datetime
    
    class Config:
        orm_mode = True
