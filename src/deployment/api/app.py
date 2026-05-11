from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'message': 'DL4AI API Running'}