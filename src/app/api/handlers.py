from src.app.api.app import app

@app.get("/")
def read_root():
    return {"Hello": "This is main metrics page"}





