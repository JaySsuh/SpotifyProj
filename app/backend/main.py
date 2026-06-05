from fastapi import FastAPI
from app.backend.api.v1.routes import auth, user, sync, recs

app = FastAPI(title="Spotify Discovery API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(sync.router, prefix="/sync", tags=["sync"])
app.include_router(recs.router, prefix="/recs", tags=["recs"])

@app.get("/")
def root():
    return {"message": "API is running"}