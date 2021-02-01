from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'MROO'}


@app.get('/testi')
def testi():
    return {'testi': 1}
