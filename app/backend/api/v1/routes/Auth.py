from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/login")
def login():
    if not SPOTIFY_CLIENT_ID or not SPOTIFY_REDIRECT_URI:
        raise HTTPException(status_code=500)