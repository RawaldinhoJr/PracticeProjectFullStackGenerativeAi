from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from core.config import settings 

app=FastAPI(
    title="Choose-Your-Adventure-Game-API",
    description="This generates Cool Stories ",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_headers=["*"],
    allow_credentials=True,
)
if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0", port=8000,reload=True)
