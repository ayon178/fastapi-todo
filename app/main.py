from fastapi import FastAPI
from mangum import Mangum  

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the TODO list API"}

# Wrap the app with Mangum for AWS Lambda compatibility
handler = Mangum(app)
