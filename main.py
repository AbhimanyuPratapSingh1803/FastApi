from fastapi import FastAPI
from Controllers.user_controller import router as user_router

app = FastAPI()

app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

@app.get("/")
def read_root():
    return {"message": "full maje"}