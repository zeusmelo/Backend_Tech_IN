from fastapi import FastAPI

# instancia da web
app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'hello world'}
