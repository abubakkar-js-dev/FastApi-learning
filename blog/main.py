from fastapi import FastAPI
from . import schemas,models
from database import engine
import uvicorn


app = FastAPI()


models.Base.metadata.create_all(bind=engine)



@app.post('/blog')
def create(request: schemas.Blog):
    return {'title': request.title, 'description': request.description, 'published': request.published}

# if __name__ == "__main__":
#     uvicorn.run(app,host='127.0.0.1',port=9000)
