from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hallo von der Survival Fox API in Docker!"}

@app.get("/status")
def read_status():
    return {
        "app": "Survival Fox API",
        "status": "ok",
        "version": "0.0.1"
    }
