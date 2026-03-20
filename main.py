from fastapi import FastAPI
from typing import Optional

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



