from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def home():
    return {'greet': {"Hello world from python fast api server"}}


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