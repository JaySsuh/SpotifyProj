import APIRouter, HTTPException
from pydantic import BaseModel
from app.backend.core.Config import settings

router = APIRouter()

class SpotifyAuthURLResponse(BaseModel):
    auth_url: str

class SpotifyCallBackResponse(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str
    expires_in: int
    
class SpotifyProfileResponse(BaseModel):
    id: str
    email: str | None = None
    display_name: str | None = None
    country: str | None = None
    
@router.get("/login", response_model=SpotifyAuthURLResponse)
async def login():
    if not settings.SPOTIFY_CLIENT_ID or not settings.SPOTIFY_REDIRECT_URI:
        raise HTTPException(status_code=500, detail="Spotify config missing")
    return {"auth_url": "placeholder"}