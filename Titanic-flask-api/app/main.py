from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'welcome'}

@app.get('/square')
def square(n: float):
    return n**2
