from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
from pydantic import BaseModel

from fastapi import FastAPI
from contextlib import asynccontextmanager
from blog.database import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic - create all tables using sync engine
    Base.metadata.create_all(bind=engine)

    yield

    # Shutdown logic (optional)
    engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Connected to Neon PostgreSQL"}


@app.get('/about')  # path operation decorator
def about():    # path operation function
    return {'data': {'This is about page'}}


@app.get('/blogs')
def blogs(limit: int = None, published: bool=True,search: Optional[str]=None):
    totalB = limit or 'All'
    # return published

    if published:
        return {'data': {f'{totalB} blogs here. (published)'}}
    else:
        return {'data': {f'{totalB} blogs here.'}}


@app.get('/blogs/{id}')
# fetch blog with id = id
def blog(id: int):
    return {'data': id}


@app.get('/blogs/{id}/comments')
def comments(id,limit=10):
    # fetch comments of blog with id = id

    return {'data': {'1', '2', '3', '4'}}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': {'all unpublished blogs'}}

class Blog(BaseModel):
    title: str
    description: str
    published: Optional[bool]=False
    publish_date: str
    comments: int

@app.post('/blogs')
def create_post(requestBlog: Blog):
    return {'data': requestBlog,'message': 'Post is created successfully'}
 


# if __name__ == "__main__":

#     uvicorn.run(app,host="127.0.0.1",port=9000)