from fastapi import FastAPI
from Controllers.user_controller import router as user_router
import os
from dotenv import load_dotenv

app = FastAPI()

app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port= os.getenv("PORT") | 8000, reload=True)

@app.get("/")
def read_root():
    return {"message": "full maje"}