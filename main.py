from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'greet':{"Hello world from python fast api server"}};


@app.get('/about')
def about():
    return {'data': {'This is about page'}}