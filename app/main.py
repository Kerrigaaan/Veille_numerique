from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get("/scrape-articles/", response_model=list[schemas.Article])
def scrape_articles(db: Session = Depends(database.SessionLocal)):
    url = "https://example-news-site.com/ai-in-medicine"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    for item in soup.find_all("div", class_="article"):
        title = item.find("h2").text.strip()
        summary = item.find("p", class_="summary").text.strip()
        url = item.find("a")["href"]
        published_at = datetime.strptime(item.find("time")["datetime"], "%Y-%m-%dT%H:%M:%SZ")

        article = schemas.ArticleCreate(title=title, summary=summary, url=url)
        db_article = crud.create_article(db=db, article=article)
        articles.append(db_article)

    return articles

@app.get("/articles/", response_model=list[schemas.Article])
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(database.SessionLocal)):
    articles = crud.get_articles(db, skip=skip, limit=limit)
    return articles
